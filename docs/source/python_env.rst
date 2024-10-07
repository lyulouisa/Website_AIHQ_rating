Set up the Python Environment
===============================

Follow these steps to first install Miniconda, and then create a Python 3.11.3 virtual environment, before proceeding with the website setup.

Step 1: Install Miniconda
-------------------------

1. Download the Miniconda installer for your operating system:
   - **Windows**: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
   - **macOS**: https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
   - **Linux**: https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

2. Follow the installation steps for your operating system:
   - **Windows**: Run the downloaded installer `.exe` file, follow the prompts, and make sure to check the box to **Add Miniconda to PATH**.
   - **macOS/Linux**:

     - **Open the Terminal**:

       - **macOS**: Press **Command (⌘) + Space**, type **Terminal**, and press Enter to open Terminal.
       - **Linux**: Press **Ctrl + Alt + T** or search for "Terminal" in your applications menu.

     - In the terminal, run the installer script by typing the following command:  

       - For macOS:
         bash Miniconda3-latest-MacOSX-x86_64.sh
       - For Linux:
         bash Miniconda3-latest-Linux-x86_64.sh

     - Follow the prompts and agree to the license terms.
     - Allow the installer to initialize Miniconda (usually by adding it to your shell's PATH).

3. Restart the Command Prompt or Terminal to complete the installation.

4. **Verify the Installation**:
   - **Open the Terminal**:
     - **Windows**: Press the **Windows Key**, type **cmd**, and press Enter to open the Command Prompt.
     - **macOS**: Press **Command (⌘) + Space**, type **Terminal**, and press Enter to open Terminal.
     - **Linux**: Press **Ctrl + Alt + T**.
   - In the terminal, type:
     conda --version

You should see the version of `conda` displayed. If not, check your PATH settings.


Step 2: Create and Activate a Python 3.11.3 Virtual Environment
---------------------------------------------------------------

1. **Open the Terminal** if it’s not already open (see Step 1 for instructions).

2. In the terminal, create a new `conda` environment with Python 3.11.3:
   conda create -n myenv python=3.11.3

   - **`myenv`** is the name of your environment. You can replace it with any name you prefer.

3. Activate the environment:
   conda activate myenv

   Your command prompt should change to indicate that the environment is active, e.g., `(myenv) C:\Users\YourName>`.


Congratulations! Now you have a python environment to run the website. You can proceed to the next section **'installation'** to get the website installed. 
