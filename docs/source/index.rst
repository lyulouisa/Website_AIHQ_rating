.. Website_AIHQ_rating documentation master file, created by
   sphinx-quickstart on Thu Oct  3 13:30:37 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Automated rating of the Ambiguous Intentions Hostility Questionnaire (automated-AIHQ)
===========================

.. image:: https://img.shields.io/badge/python-3.11-blue
   :alt: Python 3.10
   :target: https://www.python.org/downloads/release/python-3110/

.. image:: https://img.shields.io/badge/Windows-10-blue
   :alt: Windows 10
   :target: https://www.microsoft.com/windows/windows-10

.. image:: https://img.shields.io/badge/macOS-Catalina-red
   :alt: macOS Catalina
   :target: https://www.apple.com/macos/catalina/

*Automated-AIHQ* is a locally run tool that uses large language models (GPT‑3.5‑turbo and Flan‑T5‑large) to automatically score responses to the open‑ended questions in the Ambiguous Intentions Hostility Questionnaire (AIHQ).

Users prepare a .csv file containing AIHQ text responses, select one of the two models, and receive model‑generated ratings.

The tool supports both:

1. **Flan-T5-large:** Fine‑tuned on human‑rated AIHQ data. The model is downloaded to your computer and all scoring is done locally. No data is sent over the internet, making this option ideal when responses must remain fully secure and private.
2. **GPT-3.5-turbo:** The base GPT‑3.5‑turbo model (OpenAI does not permit distribution of the fine‑tuned version). This approach requires your own OpenAI API key and the text of each response is sent to OpenAI’s servers for rating.

.. raw:: html

Below you will find instructions for installation and use.

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


If you have any questions or feedback, please reach out. We’ll respond as soon as possible.
