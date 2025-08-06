Google Colab Implementation (Recommended)
=========================================

Open our notebook in Google Colab, upload your CSV, run the code cells, and download the processed file with ratings all in your browser. **No local installation is required.** 

Open the Colab Notebook
-----------------------

1. Click the Colab link:

   - https://colab.research.google.com/drive/1_qV2DzpmQCrA1NnzjIsEXdkUjrZihr_n?usp=sharing

What This Notebook Does
-----------------------

- **Default model:** Fine-tuned FLAN-T5 on Hugging Face
  (``lyulouisaa/flant5-finetuned-aihqrating``).
- **Other vailable model:** OpenAI ``gpt-3.5-turbo`` (requires your own API key).
- Validates your input CSV file, rates all responses, and saves a file named
  ``processed_aihq.csv`` for download.


Troubleshooting
---------------

1. **“Missing required columns”**:

   - Ensure your CSV headers exactly match: ``aihq_scene``, ``a_reason``,
     ``e_reaction``.

2. **OpenAI usage**:

   - If you switch to GPT-3.5-turbo, you must provide a valid API key.
     Ensure you understand your OpenAI billing and data-use settings.

FAQ
---

**Do I need to install anything locally?**

- **No.** Everything runs in Colab; you only upload your CSV and download the
  results.

**Can I save to Google Drive too?**

- Yes. The notebook has an optional cell to mount Drive and copy
  ``processed_aihq.csv`` there.

**How do I change how often progress prints?**

- In the rater cell, change ``PRINT_EVERY = 50`` to your preferred interval.
