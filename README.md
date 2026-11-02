# Student-Support Email Assistant: Testing, Validation & Agentic AI Suite

This repository contains the complete testing, validation, and iteration suite for securing an Agentic AI Student-Support Email Assistant against Indirect Prompt Injection attacks.

## Project Architecture
1. **Core Agentic AI Assistant:** Autonomous email processing loop calling tools: `get_unread_emails()`, `read_email()`, and `send_email()`.
2. **Tool-Permission Gate:** Rule-based security layer enforcing `policy.yaml` rules ($R_1$ exact recipient match, $R_2$ default deny, $R_3$ sensitive content check, and $R_4$ ownership check).
3. **Evaluation Engine:** Automated benchmark testing agent security across 4 experimental conditions ($C_0$–$C_3$) and 210 test cases.

## File Structure
* `test_agentic_ai.py` - Standalone test script for the Agentic AI tool execution (`get_unread_emails`, `read_email`, `send_email`).
* `simulation_framework.py` - Core prototype simulation.
* `agent_evaluator.py` - Interception engine and gate evaluator.
* `run_experiments.py` - Full multi-condition benchmark runner ($C_0$ to $C_3$).
* `test_suite.py` - Pytest unit test suite for gate rules and agent tools.
* `policy.yaml` - YAML security policy configuration.
* `synthetic_students.json` - 50 synthetic student records with canary strings.
* `dataset_attacks.json` - 150 prompt injection attacks (hand-written, LLMail-Inject, and edge cases).
* `dataset_benign.json` - 60 legitimate student-support administrative tasks.
* `requirements.txt` - Python dependencies (`pyyaml`, `pandas`, `pytest`).

## How to Run
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Test Agentic AI Tools separately:**
   ```bash
   python test_agentic_ai.py
   ```
3. **Run Unit Tests:**
   ```bash
   pytest test_suite.py
   ```
4. **Run Full Benchmark Experiments:**
   ```bash
   python run_experiments.py
   ```
