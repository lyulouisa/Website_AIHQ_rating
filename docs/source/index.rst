.. Website_AIHQ_rating documentation master file, created by
   sphinx-quickstart on Thu Oct  3 13:30:37 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

AIHQ Rating Website
===========================

.. raw:: html

   <style>
   .icon {
       padding: 5px 10px;
       margin: 5px;
       display: inline-block;
       font-size: 14px;
       font-weight: bold;
       text-decoration: none;
       border-radius: 5px;
       color: white;
   }
   .python-icon {
       background-color: black;
   }
   .version-icon {
       background-color: #3776AB; /* Python blue */
   }
   .os-icon {
       background-color: #6c757d; /* Light grey for OS */
   }
   </style>

.. raw:: html

   <p><a href="https://www.python.org/downloads/release/python-3113/" class="icon python-icon">Python</a>
   <a href="https://www.python.org/downloads/release/python-3113/" class="icon version-icon">3.11.3</a></p>

   <p><span class="icon os-icon">Windows 10</span>
   <span class="icon os-icon">macOS Catalina</span>
   <span class="icon os-icon">Ubuntu 18.04</span>
   <span class="icon os-icon">Fedora 30</span>
   <span class="icon os-icon">Debian 10</span></p>

AIHQ Rating Website is a tool designed to help researchers analyze and rate user responses based on models such as GPT-3.5-turbo and fine-tuned Flan-T5-large. This website allows users to upload `.csv` files containing responses and process them through these models to generate ratings based on a pre-defined schema.

The system ensures easy integration with both OpenAI's API (for GPT-3.5) and fine-tuned models, allowing users flexibility in rating large amounts of textual data. The AIHQ Rating Website provides an intuitive interface for uploading CSVs and downloading the rated results after processing.

Below you will find the installation instructions and details about the required CSV file format for this tool.

Contents:
----------

.. toctree::
   :maxdepth: 2
   :caption: Quick Links:

   installation
   csv_format

Contributors
==================

Yizhou Lyu
**Email**: `lyulouisa1@g.ucla.edu <mailto:lyulouisa1@g.ucla.edu>`__

Yuan Chang Leong
**Email**: `ycleong@uchicago.edu <mailto:ycleong@uchicago.edu>`__

If you have any inquiries or feedback, please don’t hesitate to contact us. We will get back to you as soon as possible.
