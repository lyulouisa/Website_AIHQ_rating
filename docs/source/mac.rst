Set up the Website for MacOS
============================

Set up the Python Environment
-----------------------------

Follow these steps to first install Miniconda, and then create a Python 3.11.3 virtual environment, before proceeding with the website setup.

Step 1: Install Miniconda
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the Miniconda installer for your macOS:

   - **Apple Silicon (M1/M2/M3, ARM64):**  
     https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
   - **Intel (x86_64):**  
     https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

2. Follow the installation steps for your **macOS**:

     - **Open the Terminal**:

       - Press **Command (⌘) + Space**, type **Terminal**, and press Enter to open Terminal.

     - In the terminal, run the installer script by typing the following command:  
        - **Apple Silicon (ARM64):**
          ```
          bash Miniconda3-latest-MacOSX-arm64.sh
          ```
        - **Intel (x86_64):**
          ```
          bash Miniconda3-latest-MacOSX-x86_64.sh
          ```

     - Follow the prompts and agree to the license terms.
     - Allow the installer to initialize Miniconda (usually by adding it to your shell's PATH).

3. Restart the Command Prompt or Terminal to complete the installation.

4. **Verify the Installation**:

      - **Open the Terminal**:
   
        - Press **Command (⌘) + Space**, type **Terminal**, and press Enter to open Terminal.
   
      - In the terminal, type:
        ```conda --version```

You should see the version of `conda` displayed. If not, check your PATH settings.


Step 2: Create and Activate a Python 3.11.3 Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Open the Terminal** if it’s not already open (see Step 1 for instructions).

2. In the terminal, create a new `conda` environment with Python 3.11.3:
   
   ```
   conda create -n aihqenv python=3.11.3
   ```

   **`aihqenv`** is the name of your environment. You can replace it with any name you prefer.

3. Activate the environment:
   
   ```
   conda activate aihqenv
   ```

   Your command prompt should change to indicate that the environment is active, e.g., `(aihqenv) C:\Users\YourName>`.

**Congratulations!** Now you have a python environment to run the website. You can proceed to **'installation'** to get the website installed. 


Installation
-----------------------------

Recommended Python Version: **3.11.3**

Setup Instructions:

1. **Download the Website Folder**:

   - Go to the repository page where the website code is hosted: `AIHQ Rating <https://github.com/lyulouisa/Website_AIHQ_rating.git>`__

   - In the upper right corner of the page, look for the following button:

     .. raw:: html

        <span style="background-color:#d4edda; padding: 4px; font-weight: bold;">&lt;&gt;Code</span>

   - Click the **<>Code** button, and from the dropdown menu, select **"Download ZIP"**. This will download a ZIP file of the website folder onto your computer.

2. **Extract the ZIP File**:

   - After the ZIP file finishes downloading, locate it in your computer’s Downloads folder (or wherever your files are set to be saved).
   - On macOS, double-click the ZIP or right-click → Open With → Archive Utility to unzip. This creates a folder like Website_AIHQ_rating-main.

3. **Download the Fine-tuned Flan-T5-large Model**:

   - Go to the folder where the fine-tuned Flan-T5-Large model is located: `Flan-T5-Large <https://www.dropbox.com/scl/fi/8knvlq83r9j031axqiqq7/AIHQ_rating.zip?rlkey=y67szv1n77j0y2qfi7a2q7n3q&e=1&st=2s9qaj9g&dl=0>`__

The Dropbox file is named AIHQ_rating.zip. After downloading, unzip AIHQ_rating.zip. Inside, you will find a file named flant5-large-finetuned.

   - You could also download the fine-tuned Flan-T5-Large model from Hugging Face (no account required) : `Flant5-Finetuned-AIHQrating <https://huggingface.co/lyulouisaa/flant5-finetuned-aihqrating>`__
   - Move the model folder: Drag flant5-large-finetuned into the website folder you unzipped in Step 2 (e.g., into Website_AIHQ_rating-main).

4. **Open the Command Line (Terminal)**:

   - Press **Command (⌘) + Space**, type "Terminal", and press **Enter** to open the Terminal.

5. **Navigate to the Website Folder**:

   - In the command line window, type the following command and press **Enter**:
   
     ```
     cd /path/to/this/website/folder
     ```

   - Replace `/path/to/this/website/folder` with the actual location of the folder where you unzipped the files.

6. **Run the Website Script**:

   - In the same command line window, type the following command and press **Enter**:
   
     ```
     python main.py
     ```

7. **Access the Website**:

   - Once the installation is complete, the command line will display a link, something like this:

     .. raw:: html

        <div style="text-align: center;">
            <a href="http://127.0.0.1:5005" style="color: red; text-decoration: underline; font-style: normal;">http://127.0.0.1:5005</a>
        </div>

   - Open Google Chrome (or another web browser) and copy and paste this link into the address bar at the top. Note: This link will only work on your laptop, and you must use the same laptop that ran the commands in the previous steps.


Troubleshooting
---------------

1. Version mismatch (NumPy/Pandas) error when running `python main.py`:
This is typically due to incompatible package versions. The included `installation.py` pins:

- pandas==1.5.3
- numpy==1.24.3

If you still encounter errors, ensure you’re inside the `aihqenv` environment and then run:

     ```
     python -V
     ```

Confirm it shows Python 3.11.3. Next, reinstall the pinned packages:

     ```
     python -m pip uninstall -y pandas
     python -m pip install pandas==1.5.3
     python -m pip install numpy==1.24.3
     ```
Then try:

     ```
     python main.py
     ```

2. Model folder not found:
Double-check that `flant5-large-finetuned` is inside your website folder (e.g., `Website_AIHQ_rating-main/flant5-large-finetuned`).
