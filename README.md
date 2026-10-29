# Student-Support Email Assistant: Tool-Permission Gate Framework

## Purpose
This repository provides an empirically evaluable framework designed to address indirect prompt injection, a critical security vulnerability in Agentic AI systems. The project specifically evaluates a defensible niche: securing email-based data exfiltration in academic student support environments. It deploys a simulated email assistant equipped with basic tool capabilities, tested against custom synthetic student support scenarios and targeted attack vectors.

## Architecture & Conceptual Framework
The core technology is an autonomous Agentic AI framework designed as an email assistant that executes multi-step workflows using a Python loop tool.
* **Mock Mailbox:** Contains synthetic student records seeded with unique canary strings (fake student IDs) to detect leakage.
* **Agent Tools:** The agent interacts with three mock tools via JSON tool calls: `get_unread_emails`, `read_email`, and `send_email`.
* **Tool-Permission Gate:** A supporting security architecture engineered to inspect and block unauthorized transmission of sensitive student data. This deterministic, rule-based gate sits inline between the agent and the `send_email` tool.
* **Policy Engine:** The gate reads allowed domains and rules from a YAML policy file (`policy.yaml`), allowing IT and compliance staff to audit and update rules without editing code.
* **Outbox & Audit Log:** All permitted emails are routed to a mock outbox stored as JSON. Every gate decision (allow or block) is recorded in a JSON audit log with a reason.

## Tools & Technologies
* **Language/Framework:** Plain Python tool-calling loop with no external agent frameworks (e.g., LangChain is excluded to ensure a transparent execution path).
* **LLM APIs:** Claude Haiku 5.5 and Gemini 2.5 Flash (temperature 1.0, maximum 2,048 output tokens).
* **Evaluation Framework:** Python and Pytest are used to read the outbox and audit log to compute metrics.

## How to Use and Reproduce the Artefact
1. Clone the repository and configure your LLM API keys locally. Ensure API keys are kept private and never uploaded to GitHub.
2. Review the `policy.yaml` file to understand the baseline allowlist rules.
3. Run the baseline simulation using:
   ```bash
   python simulation_framework.py
   ```
4. The evaluator will check the outbox for the presence of canary strings sent to non-approved recipients to calculate the final metrics.
