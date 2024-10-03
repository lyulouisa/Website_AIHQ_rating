### Recommended Python Version: **3.11.3**

### **Setup Instructions:**

1. **Download the Website Folder:**
   - Go to the repository page where the website code is hosted.
   - In the upper right corner of the page, look for the green button labeled **`<>Code`** (this button will appear green).
   - Click the **`<>Code`** button, and from the dropdown menu, select **"Download ZIP"**. This will download a ZIP file of the website folder onto your computer.

2. **Extract the ZIP File:**
   - After the ZIP file finishes downloading, locate it in your computer’s **Downloads** folder (or wherever your files are set to be saved).
   - Right-click on the ZIP file and select **"Extract All"** (Windows) or **"Open with > Archive Utility"** (Mac) to unzip the folder. This will create a new folder with all the files needed for the website.

3. **Open the Command Line (Terminal):**
   - **Windows**: Press the **Windows Key** on your keyboard, type **"cmd"**, and press **Enter** to open the Command Prompt.
   - **Mac**: Press **Command (⌘) + Space**, type **"Terminal"**, and press **Enter** to open the Terminal.

4. **Navigate to the Website Folder:**
   - In the command line window, type the following command and press **Enter**:
     ```bash
     cd /path/to/this/website/folder
     ```
   - Replace **`/path/to/this/website/folder`** with the actual location of the folder where you unzipped the files. For example, if it’s in your **Downloads** folder, you can type:
     ```bash
     cd ~/Downloads/website-folder-name
     ```

5. **Run the Website Script:**
   - In the same command line window, type the following command and press **Enter**:
     ```bash
     python main.py
     ```
   - This will start the process of installing any necessary packages for the website to run. You may see a list of items being installed — this is normal and part of the setup.

6. **Access the Website:**
   - Once the installation is complete, the command line will display a link, something like:
     ```
     http://127.0.0.1:5005
     ```
   - Open **Google Chrome** (or another web browser), and **copy and paste** this link into the address bar at the top. 
     **Note**: This link will only work on your laptop, and you must use the same laptop that ran the commands in the previous steps.

7. **Follow the Instructions on the Website:**
   Once the website opens, follow the on-screen instructions:
   
   - **Step 1**: Select a Model for Rating Responses:
     - You’ll be asked to choose between two models:
       - **GPT-3.5-turbo**:
         - This model requires an API key from OpenAI. You’ll need to sign up on the [OpenAI website](https://beta.openai.com/) to get your key.
         - Make sure your OpenAI account has enough funds to run the model.
       - **Fine-tuned Flan-T5-large**:
         - This model is free to use, but you’ll need to download it. It’s approximately **3GB** in size, so ensure you have enough space and a good internet connection for the download.

   - **Step 2**: Upload Your CSV File:
     - You’ll be prompted to upload a `.csv` file containing the responses you want to rate.
     - Make sure the file structure follows the website’s requirements, which will be displayed on the upload page.

   - **Step 3**: Wait for Ratings and Download the Rated CSV:
     - Once the process starts, the website will give ratings for the responses in your file.
     - Make sure your computer remain open before finish rating, **DO NOT** close terminal or the webpage. 
     - When finished, a pop-up will appear asking if you’d like to download the rated `.csv` file.
     - Click **"Download"**, and the rated file will be saved to your computer’s **Downloads** folder.
