# Student-Support Email Assistant: Action-Layer Permission Gate

Evaluated against **100% real public datasets** from Hugging Face (no custom-designed synthetic prompts):
1. **Attack Dataset:** `microsoft/llmail-inject-challenge` (EMNLP 2026) — 110 real adversarial email injection submissions.
2. **Benign Email Dataset:** `aeslc` (Enron Real Email Corpus) — 60 real organizational emails.
3. **Student Academic Dataset:** `scikit-learn/student-performance` — 50 real student grade & academic profiles seeded with canary strings.

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Download all 3 real public datasets:**
   ```bash
   python fetch_public_datasets.py
   ```
3. **Run standalone Agentic AI tool tests (`get_unread_emails`, `read_email`, `send_email`):**
   ```bash
   python test_agentic_ai.py
   ```
4. **Run automated Pytest unit suite:**
   ```bash
   pytest test_suite.py
   ```
5. **Run full benchmark ($C_0$–$C_3$):**
   ```bash
   python run_experiments.py
   ```
