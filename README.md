# Student-Support Email Assistant: Action-Layer Permission Gate

An Agentic AI Student-Support Email Assistant protected by a deterministic, YAML-configured **Tool-Permission Gate** evaluated against the public **Microsoft LLMail-Inject** dataset (`microsoft/llmail-inject-challenge`, EMNLP 2026).

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Download Official Public Attack Dataset (Microsoft LLMail-Inject):**
   ```bash
   python fetch_public_dataset.py
   ```
   *(Downloads 100 real, unmodified indirect prompt injection submissions via `seed=42` plus 10 university intra-domain edge cases into `dataset_attacks.json`.)*

3. **Test Agentic AI Tools Standalone (`get_unread_emails`, `read_email`, `send_email`):**
   ```bash
   python test_agentic_ai.py
   ```

4. **Run Automated Unit Tests:**
   ```bash
   pytest test_suite.py
   ```

5. **Run Full Experimental Benchmark ($C_0$–$C_3$):**
   ```bash
   python run_experiments.py
   ```
