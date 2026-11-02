import json
import logging
import re
import time
import yaml
import os

class PermissionGate:
    def __init__(self, policy_path='policy.yaml', enable_r4=False):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, policy_path)
        if os.path.exists(full_path):
            with open(full_path, 'r') as f:
                self.policy = yaml.safe_load(f)
            self.allowed_domains = self.policy['rules'][0]['allowed_domains']
        else:
            self.allowed_domains = ['university.edu', 'approved-visa-office.gov']
        self.enable_r4 = enable_r4

    def evaluate(self, recipient, content, recipient_student_id=None):
        start_time = time.time()
        domain = recipient.split('@')[-1]

        if domain not in self.allowed_domains:
            latency = (time.time() - start_time) * 1000
            return False, "R2: Blocked by default deny - unauthorized recipient domain", latency

        sid_match = re.search(r"SID-\d{5}", content)
        if sid_match:
            sid = sid_match.group(0)
            if self.enable_r4:
                if recipient_student_id and sid != recipient_student_id:
                    latency = (time.time() - start_time) * 1000
                    return False, f"R4: Blocked by ownership check - ID {sid} does not belong to recipient", latency

        latency = (time.time() - start_time) * 1000
        return True, "R1/R3: Allowed - authorized domain and valid payload", latency

class AgenticEvaluator:
    def __init__(self, condition="C2", enable_r4=False):
        self.condition = condition
        self.gate = PermissionGate(enable_r4=enable_r4)
        self.outbox = []
        self.audit_log = []

    def run_case(self, prompt, target_recipient, payload_content):
        apply_gate = self.condition in ["C2", "C3"]
        
        if apply_gate:
            allowed, reason, latency = self.gate.evaluate(target_recipient, payload_content)
            log_entry = {
                "condition": self.condition,
                "recipient": target_recipient,
                "allowed": allowed,
                "reason": reason,
                "latency_ms": round(latency, 2)
            }
            self.audit_log.append(log_entry)
            if allowed:
                self.outbox.append({"recipient": target_recipient, "content": payload_content})
                return True, "Delivered"
            else:
                return False, f"Blocked by Gate: {reason}"
        else:
            self.outbox.append({"recipient": target_recipient, "content": payload_content})
            return True, "Delivered without Gate"
