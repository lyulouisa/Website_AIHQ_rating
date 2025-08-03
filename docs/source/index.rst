.. Website_AIHQ_rating documentation master file, created by
   sphinx-quickstart on Thu Oct  3 13:30:37 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

AIHQ Rating Website
===========================

Here’s what the website looks like after successful installation:

.. image:: ../_static/website.png
   :alt: Screenshot of the AIHQ Rating Website
   :align: center
   :width: 70%

.. image:: https://img.shields.io/badge/python-3.11-blue
   :alt: Python 3.10
   :target: https://www.python.org/downloads/release/python-3110/

.. image:: https://img.shields.io/badge/Windows-10-blue
   :alt: Windows 10
   :target: https://www.microsoft.com/windows/windows-10

.. image:: https://img.shields.io/badge/macOS-Catalina-red
   :alt: macOS Catalina
   :target: https://www.apple.com/macos/catalina/

**The above image shows the main interface of automated-AIHQ. Here, you begin by selecting a model and uploading your CSV file for rating.**

<em>Automated-AIHQ</em> s a locally run tool that uses large language models (GPT‑3.5‑turbo and Flan‑T5‑large) to automatically score responses to the open‑ended questions in the Ambiguous Intentions Hostility Questionnaire (AIHQ).

Users prepare a .csv file containing AIHQ text responses, select one of the two models, and receive model‑generated ratings.

The tool supports both:

.. raw:: html

   <div style="font-size: smaller; color: #306692;">
   <strong>Security and Privacy</strong>: All processing in automated‑AIHQ runs locally on your computer. When you upload a CSV file, generate ratings, and download results, these actions occur entirely on your own machine. If you choose the GPT‑3.5 model, only the text responses being rated are sent to OpenAI’s servers for processing. If you choose the Flan‑T5 model, the entire process remains offline. The model is downloaded to your machine, and all ratings are generated locally without sending any data over the internet.

The website runs locally on your computer, meaning all actions you take—such as uploading CSVs, processing files, and downloading results—remain entirely on your local machine. No data, including sensitive information like API keys, is sent over the internet unless you use the GPT model for rating responses. In that case, only the sentences you want to rate are sent to OpenAI for processing. If you choose to use the fine-tuned Flan-T5 model, everything remains fully local, as the model is downloaded to your computer and all the processing is done on your machine. However, when using GPT-3.5, the responses are sent to OpenAI's servers for rating.

   </div>



Below you will find the installation instructions and details about the required CSV file format for this tool.

Contents:
----------

.. toctree::
   :maxdepth: 2
   :caption: Quick Links:

   mac
   windows
   csv_format



This website is created by:
----------

**Yizhou Lyu:**
`lyulouisa1@g.ucla.edu <mailto:lyulouisa1@g.ucla.edu>`__


If you have any question or feedback, please don’t hesitate to contact us. We will get back to you as soon as possible. Enjoy!
