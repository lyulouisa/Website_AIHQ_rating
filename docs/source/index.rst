.. Website_AIHQ_rating documentation master file, created by
   sphinx-quickstart on Thu Oct  3 13:30:37 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

AIHQ Rating Website
===========================

Here’s what the website looks like after installation:

.. image:: ../_static/website.png
   :alt: Screenshot of the AIHQ Rating Website
   :align: center
   :width: 800px

**The above image shows the main page of the AIHQ Rating Website, where you can start by selecting a model and uploading your CSV file for rating.**

AIHQ Rating Website is a website designed to help researchers rate responses to open-ended questions in the Ambiguous Intentions Hostility Questionnaire (AIHQ) using large language models such as GPT-3.5-turbo and Flan-T5-large specifically fine-tuned for AIHQ rating. This website allows users to upload `.csv` files containing responses and process them through one of the two models to generate ratings like trained human raters do.

The system ensures easy integration with both OpenAI's API (for GPT-3.5) and the Flan-t5 language model, allowing users flexibility in rating large amounts of textual data. The AIHQ Rating Website provides an intuitive interface for uploading CSVs and downloading the rated results after processing.

**Security and Privacy**: The website runs locally on your computer, meaning all actions you take—such as uploading CSVs, processing files, and downloading results—remain entirely on your local machine. No data, including sensitive information like API keys, is sent over the internet unless you use the GPT model for rating responses. In that case, only the sentences you want to rate are sent to OpenAI for processing.

If you choose to use the fine-tuned Flan-T5 model, everything remains fully local, as the model is downloaded to your computer and all the processing is done on your machine. However, when using GPT-3.5, the responses are sent to OpenAI's servers for rating.

Below you will find the installation instructions and details about the required CSV file format for this tool.

Contents:
----------

.. toctree::
   :maxdepth: 2
   :caption: Quick Links:

   installation
   csv_format



Contributors
----------

**Yizhou Lyu:**
`lyulouisa1@g.ucla.edu <mailto:lyulouisa1@g.ucla.edu>`__

**Yuan Chang Leong:**
`ycleong@uchicago.edu <mailto:ycleong@uchicago.edu>`__

If you have any question or feedback, please don’t hesitate to contact us. We will get back to you as soon as possible. Enjoy!
