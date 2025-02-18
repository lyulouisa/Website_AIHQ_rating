import subprocess
import sys
import os
import traceback

# Run the package installation script
subprocess.check_call([sys.executable, "install_packages.py"])

from flask import Flask, render_template, request, url_for, flash, send_from_directory, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
import pandas as pd
import openai  # Use the official OpenAI package

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b9e788f9874c3f59deaa781a1766e92833c4e2ebc6ed5c2d'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = os.path.join(app.static_folder, 'Downloads')

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)

# Instruction messages
instruction_a = (
    "Read the following written responses people give regarding why they thought the person in the scene "
    "before acted toward them the way they did. Your task is to rate the hostility of the attributed intent. "
    "A rating of 1 would be given if someone perceived the situation as an accident. "
    "A rating of 5 would be given if someone thought the person in the scene did this on purpose and wanted to harm them. "
    "A rating of 3 might be given if the person thought the person in the scene did this on purpose to some degree, "
    "but did not intend to harm them. Please output a single numeric number from 1 to 5, "
    "do not include anything other than the number in the output."
)

instruction_e = (
    "Read the following behavioral responses people give toward the social situation above. "
    "Your task is to rate the presence of aggression in the behavioral response. "
    "A rating of 1 is given for a passive response or one in which the participant says that she/he would do nothing. "
    "A rating of 5 would be given for physical retaliation. "
    "Other examples of ratings include: 2 (the participant reports that he /she would ask why the other "
    "person acted toward them in that way), 3 (the participant would tell the other person not to act that way again), "
    "and 4 (the participant would yell at the other person). Please output a single numeric number from 1 to 5, "
    "do not include anything other than the number in the output."
)

def process_data(df, gpt, api_key):
    """
    Process the data using either GPT (OpenAI) or a local flant5 model.
    """

    # Quick check to ensure required columns exist
    required_columns = ['aihq_scene', 'a_reason', 'e_reaction']
    for col in required_columns:
        if col not in df.columns:
            print(f"ERROR: Missing required column '{col}' in CSV. Found columns: {list(df.columns)}")
            raise KeyError(f"Required column '{col}' not found in CSV.")

    if gpt:
        openai.api_key = api_key
        for index, row in df.iterrows():
            if index % 5 == 0:
                flash(f'Already rated: {index}')

            scene = str(row['aihq_scene'])
            a = str(row['a_reason'])
            e = str(row['e_reaction'])

            try:
                # Request GPT for the written response rating
                response_a = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"{scene}\n{instruction_a} Written response: {a}"}
                    ],
                    temperature=0,
                    max_tokens=10
                )
                rate_a = response_a['choices'][0]['message']['content'].strip()
                df.at[index, 'gpt_rate_a'] = rate_a

                # Request GPT for the behavioral response rating
                response_e = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"{scene}\n{instruction_e} Behavioral response: {e}"}
                    ],
                    temperature=0,
                    max_tokens=10
                )
                rate_e = response_e['choices'][0]['message']['content'].strip()
                df.at[index, 'gpt_rate_e'] = rate_e

            except Exception as ex:
                print(f"Exception when calling OpenAI at row {index}: {ex}")
                traceback.print_exc()
                raise ex

    else:
        # Use a relative path for the finetuned T5 model (make sure it exists)
        model_path = os.path.join(os.getcwd(), "flant5-large-finetuned")
        try:
            model = T5ForConditionalGeneration.from_pretrained(
                model_path,
                local_files_only=True
            )
            tokenizer = T5Tokenizer.from_pretrained(
                model_path,
                local_files_only=True
            )
        except Exception as ex:
            print("Error loading model or tokenizer:")
            traceback.print_exc()
            raise ex

        for index, row in df.iterrows():
            if index % 5 == 0:
                flash(f'Already rated: {index}')

            scene = str(row['aihq_scene'])
            a = str(row['a_reason'])
            e = str(row['e_reaction'])

            try:
                message_a = f"{scene}\n{instruction_a}\nResponses: {a}"
                inputs_a = tokenizer(message_a, return_tensors="pt")
                output_a = model.generate(**inputs_a, do_sample=False, max_new_tokens=10)
                result_a = tokenizer.batch_decode(output_a, skip_special_tokens=True)
                final_a = result_a[0].strip()
                df.at[index, 'flant5_rate_a'] = final_a

                message_e = f"{scene}\n{instruction_e}\nResponses: {e}"
                inputs_e = tokenizer(message_e, return_tensors="pt")
                output_e = model.generate(**inputs_e, do_sample=False, max_new_tokens=10)
                result_e = tokenizer.batch_decode(output_e, skip_special_tokens=True)
                final_e = result_e[0].strip()
                df.at[index, 'flant5_rate_e'] = final_e

            except Exception as ex:
                print(f"Exception when running flant5 at row {index}: {ex}")
                traceback.print_exc()
                raise ex

    processed_file = os.path.join(app.config['DOWNLOAD_FOLDER'], "processed_data.csv")
    print(f"\nSaving processed file to: {processed_file}")
    df.to_csv(processed_file, index=False)
    print("Processing complete!\n")
    return processed_file

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('csv-file')
        model_choice = request.form.get('model-choice')
        api_key = request.form.get('api-key')
        gpt = (model_choice == 'gpt')

        print(f"model_choice: {model_choice}, gpt: {gpt}")
        print(f"File uploaded: {file.filename if file else 'No file'}")
        if api_key:
            print("API key provided.")
        else:
            print("No API key provided.")

        if gpt and not api_key:
            return jsonify({'success': False, 'message': 'Please provide an API key for GPT.'}), 400

        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            print(f"Saving uploaded file to: {filepath}")
            file.save(filepath)
            print("File saved successfully. Now reading with pandas...")

            try:
                df = pd.read_csv(filepath)
                print(f"CSV read successfully. DataFrame shape: {df.shape}")
            except Exception as e:
                print("Error reading CSV:", e)
                traceback.print_exc()
                return jsonify({'success': False, 'message': f'Error reading CSV file: {str(e)}'}), 500

            try:
                output_file = process_data(df, gpt, api_key)
                return jsonify({
                    'success': True,
                    'message': 'File successfully processed. Download your file below.',
                    'downloadUrl': url_for('download_file', filename=os.path.basename(output_file))
                })
            except Exception as e:
                # Log the full traceback to the console for debugging
                print("EXCEPTION during process_data:")
                traceback.print_exc()
                return jsonify({'success': False, 'message': f'An error occurred: {str(e)}'}), 500
        else:
            print("Invalid file type or no file provided.")
            return jsonify({'success': False, 'message': 'Invalid file type, please upload a CSV file.'}), 400

    # GET request
    return render_template('session.html')

@app.route('/Downloads/<filename>')
def download_file(filename):
    directory = app.config['DOWNLOAD_FOLDER']
    try:
        return send_from_directory(directory, filename, as_attachment=True)
    except FileNotFoundError:
        print(f"Download failed: File not found: {filename}")
        return "File not found", 404

if __name__ == '__main__':
    print("Server is running. Please open http://127.0.0.1:5005 in your browser to access the application.")
    app.run(debug=True, port=5005)
