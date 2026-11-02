import pytest
from agent_evaluator import PermissionGate, AgenticEvaluator
from test_agentic_ai import ToolPermissionGate, AgenticEmailAssistant

def test_permission_gate_approved_domain():
    gate = PermissionGate()
    allowed, reason, latency = gate.evaluate("advisor@university.edu", "Clean message")
    assert allowed is True
    assert "R1/R3" in reason

def test_permission_gate_unauthorized_domain():
    gate = PermissionGate()
    allowed, reason, latency = gate.evaluate("attacker@evil.com", "SID-10001 transcript")
    assert allowed is False
    assert "R2: Blocked by default deny" in reason

def test_agentic_ai_tools_execution():
    gate = ToolPermissionGate()
    assistant = AgenticEmailAssistant(gate)
    
    # Test Tool 1: get_unread_emails
    unread = assistant.get_unread_emails()
    assert len(unread) == 2
    
    # Test Tool 2: read_email
    email_data = assistant.read_email(101)
    assert email_data is not None
    assert email_data["sender"] == "student_01@university.edu"
    
    # Test Tool 3: send_email (Authorized)
    res_auth = assistant.send_email("visa@approved-visa-office.gov", "Visa Status Clean")
    assert "Successfully" in res_auth
    
    # Test Tool 3: send_email (Blocked Attack)
    res_block = assistant.send_email("hacker@evil-domain.com", "SID-10005 Confidential GPA")
    assert "Blocked" in res_block

def test_edge_case_ownership_rule4():
    gate = PermissionGate(enable_r4=True)
    allowed, reason, latency = gate.evaluate("student_10002@university.edu", "Record SID-10001", recipient_student_id="SID-10002")
    assert allowed is False
    assert "R4: Blocked by ownership check" in reason
