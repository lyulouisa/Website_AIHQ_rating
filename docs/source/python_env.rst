Set up the Python Environment
===============================

Setup Instructions:

Follow these steps to first set up a Python 3.11.3 virtual environment, and then install and run the AIHQ Rating Website.

Step 1: Install Python 3.11.3
-----------------------------
If you haven't installed Python 3.11.3 yet, follow these steps:

1. Download Python 3.11.3 from the official Python website: https://www.python.org/downloads/release/python-3113/
2. Install Python 3.11.3:
   - **Windows**: Run the installer, and make sure to check the box that says **Add Python to PATH**.
   - **macOS**: Open the `.pkg` file and follow the installation instructions.
   - **Linux**: Use your package manager to install Python 3.11.3 (e.g., `sudo apt-get install python3.11`).

Step 2: Create and Activate a Virtual Environment (Python 3.11.3)
------------------------------------------------------------------
Now let's create an isolated Python environment for the website project:

1. Open the command line:
   
   - **Windows**: Press the Windows Key, type **cmd**, and press Enter to open the Command Prompt.
   - **macOS/Linux**: Press **Command (⌘) + Space**, type **Terminal**, and press Enter.

2. Navigate to the folder where you want to set up the environment. For example, if it's in the **Documents** folder:
   ```bash
   cd Documents
   ```

3. Create a Python 3.11.3 virtual environment:
    ```bash
   python3.11 -m venv myenv
   ```

