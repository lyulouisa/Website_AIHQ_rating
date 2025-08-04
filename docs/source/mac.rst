Set up the Website for MacOS
============================

1. Prepare Python Environment
-----------------------------

You will first install Miniconda, then create a Python 3.11.3 virtual environment.

Step 1: Install Miniconda
~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Download the correct installer for your Mac:**

   - **Apple Silicon (M1/M2/M3, ARM64):**  
     https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
   - **Intel (x86_64):**  
     https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

2. **Open Terminal:**

   - Press **Command (⌘) + Space**, type **Terminal**, and press **Enter**

3. **Run the installer for Miniconda:**

   - **Apple Silicon (ARM64):** ::

       bash Miniconda3-latest-MacOSX-arm64.sh

   - **Intel (x86_64):** ::

       bash Miniconda3-latest-MacOSX-x86_64.sh

     - Follow the prompts and agree to the license terms.  
     - Allow the installer to initialize Miniconda (usually by adding it to your shell’s PATH).

4. **Restart Terminal and verify installation.**

   - Open Terminal (same shortcut as above).  
   - In the terminal window, type ::

       conda --version

   - You should see the conda version displayed. If not, check your `PATH` settings.

Step 2: Create and Activate a Python 3.11.3 Virtual Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Open Terminal (see Step 1.2).

2. Create a new Python 3.11.3 conda environment: ::

       conda create -n aihqenv python=3.11.3

   *(“aihqenv” is just a name—you may choose something else.)*

3. Activate the environment: ::

       conda activate aihqenv

   Your prompt should now show ``(aihqenv)`` to indicate the environment is active.

2. Install automated-AIHQ
-------------------------

Step 1: Download the automated-AIHQ
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Visit the repository page:  
   ``https://github.com/lyulouisa/Website_AIHQ_rating``

   - At the top-right area of the page, just above the list of files, you’ll see a green button labeled  

     .. raw:: html

        <span style="background-color:#d4edda; padding:4px; font-weight:bold;">&lt;&gt;Code</span>

   - Click the **<> Code** button, and in the menu that appears, choose **“Download ZIP.”**  
     This downloads *Website_AIHQ_rating-main.zip*.

2. **Extract the ZIP file:**

   - Locate *Website_AIHQ_rating-main.zip* in your Downloads folder.  
   - Double-click the ZIP (or right-click → *Open With → Archive Utility*).  
   - You should now see a folder called *Website_AIHQ_rating-main*—this is the automated-AIHQ tool.

3. **Download the fine-tuned Flan-T5-large model** *(skip if you won’t use this model)*

   i.  **Zenodo:** ``https://zenodo.org/records/16730672``  
   ii. **Dropbox:** ``https://www.dropbox.com/scl/fi/8knvlq83r9j031axqiqq7/AIHQ_rating.zip?dl=0``  
   iii. **Hugging Face:** ``https://huggingface.co/lyulouisaa/flant5-finetuned-aihqrating``  
        *(download each file into a folder named ``flant5-finetuned-aihqrating``)*

   - After downloading, double-click to unzip. You should see a folder named *flant5-large-finetuned*.

4. **Place the model folder in *Website_AIHQ_rating-main***

   - Drag *flant5-large-finetuned* into *Website_AIHQ_rating-main*.  
   - Your folder structure should now look like:

     ::
       Website_AIHQ_rating-main/
       ├── flant5-large-finetuned/
       ├── main.py
       └── …

5. **Open Terminal** and **navigate** to the tool’s folder: ::

       cd /path/to/Website_AIHQ_rating-main

6. **Run the script:** ::

       python main.py

7. **Access the automated-AIHQ interface:**

   - When the server starts, Terminal prints something like:

     .. raw:: html

        <div style="text-align:center;">
          <a href="http://127.0.0.1:5005" style="color:red; text-decoration:underline;">http://127.0.0.1:5005</a>
        </div>

   - Open that link in your browser; the interface appears.

Troubleshooting
---------------

1. **Version mismatch (NumPy/Pandas) error when running ``python main.py``**

   The bundled ``installation.py`` pins:

   - pandas==1.5.3  
   - numpy==1.24.3  

   Ensure you’re in the ``aihqenv`` environment, then check Python: ::

       python -V

   It should show **Python 3.11.3**. If errors persist, reinstall the pinned packages: ::

       python -m pip uninstall -y pandas
       python -m pip install pandas==1.5.3
       python -m pip install numpy==1.24.3

   Finally, rerun: ::

       python main.py

2. **Model folder not found**

   Verify that ``flant5-large-finetuned`` sits inside your website folder, e.g.:

   ::
     Website_AIHQ_rating-main/flant5-large-finetuned

