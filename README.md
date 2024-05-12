### Recommended Python version: 3.11.3

**Setup Instructions:**

1. **Navigate to the directory of the website:**
   ```bash
   cd /path/to/this/website/folder
   ```
2. **Run the following command in the command line:**
   ```bash
   python main.py
   ```
   This command should start the installation of necessary packages, and as soon as all packages are installed, a local website link should appear.
3. **Copy the local website link into your web browser(recommend Google Chrome):**

   http://127.0.0.1:5005

   Note that the link ONLY works on your laptop and you MUST open the link on the same laptop that ran the aforementioned commands.
4. **Follow the instructions on the website:**
   - **First select between two models**:
     - *GPT-3.5-turbo*: Delivers reliable performance closely aligned with human ratings.
       - Obtain an API key from OpenAI API.
       - Verify that your API account has sufficient funds.
     - *Fine-tuned Flan-T5-large*: Offers reliable performance at no cost.
       - Download the model, approximately 3GB in size.
   - **Then upload the .csv that contain the responses you want to rate**:
     - Make sure your .csv has the correct file structure according to requirements on the website.
   - **Lastly, wait, and download the rated .csv when it's finished**:
     - A window will pop up asking if you want to download the rated responses when rating is finished
     - The rated responses will be downloaded to your /download folder.
