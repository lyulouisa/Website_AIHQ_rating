Set up the Website for Windows System
===============================

Set up the Python Environment
-----------------------------

Follow these steps to first install Miniconda, and then create a Python 3.11.3 virtual environment, before proceeding with the website setup.

Step 1: Install Miniconda
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download the Miniconda installer for your Windows: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

2. Find the installer package in your Downloads folder. Follow the installation steps for your Windows:

      - Run the downloaded installer `.exe` file, follow the prompts, and make sure to check the box to **Add Miniconda to PATH**.

3. Restart the Command Prompt or Terminal to complete the installation.

4. **Verify the Installation**:

      - **Open the Terminal**:
   
        - Press the **Windows Key**, type **cmd**, and press Enter to open the Command Prompt.
   
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

   - **`aihqenv`** is the name of your environment. You can replace it with any name you prefer.

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
   - Right-click on the ZIP file and select **"Extract All"** (Windows) or **"Open with > Archive Utility"** (Mac) to unzip the folder.

3. **Open the Command Line (Terminal)**:

   - **Windows**: Press the **Windows Key** on your keyboard, type "cmd", and press **Enter** to open the Command Prompt.
   - **Mac**: Press **Command (⌘) + Space**, type "Terminal", and press **Enter** to open the Terminal.

4. **Navigate to the Website Folder**:

   - In the command line window, type the following command and press **Enter**:
   
     ```
     cd /path/to/this/website/folder
     ```

   - Replace `/path/to/this/website/folder` with the actual location of the folder where you unzipped the files.

5. **Run the Website Script**:

   - In the same command line window, type the following command and press **Enter**:
   
     ```
     python main.py
     ```

6. **Access the Website**:

   - Once the installation is complete, the command line will display a link, something like this:

     .. raw:: html

        <div style="text-align: center;">
            <a href="http://127.0.0.1:5005" style="color: red; text-decoration: underline; font-style: normal;">http://127.0.0.1:5005</a>
        </div>

   - Open Google Chrome (or another web browser) and copy and paste this link into the address bar at the top. Note: This link will only work on your laptop, and you must use the same laptop that ran the commands in the previous steps.
