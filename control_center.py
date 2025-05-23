
import json
import random
import time

class ControlCenter:
    def __init__(self, config_path='core/shadow_swd.json'):
        with open(config_path, 'r') as f:
            self.data = json.load(f)

    def get_target_info(self, target_domain):
        return self.data.get('targets', {}).get(target_domain, {})

    def get_headers(self, target_domain):
        info = self.get_target_info(target_domain)
        return info.get('headers', {})

    def get_payloads(self, target_domain):
        info = self.get_target_info(target_domain)
        return info.get('payloads', [])

    def get_tactic(self, target_domain):
        info = self.get_target_info(target_domain)
        return info.get('tactic', 'default')

    def get_obfuscation(self, target_domain):
        info = self.get_target_info(target_domain)
        return info.get('obfuscation_style', 'none')

    def get_delay(self, target_domain):
        info = self.get_target_info(target_domain)
        return info.get('delay', 0)

    def simulate_behavior(self, target_domain):
        delay = self.get_delay(target_domain)
        if delay > 0:
            time.sleep(delay)
        headers = self.get_headers(target_domain)
        payloads = self.get_payloads(target_domain)
        tactic = self.get_tactic(target_domain)
        obfuscation = self.get_obfuscation(target_domain)
        return {
            "headers": headers,
            "payload": random.choice(payloads) if payloads else "",
            "tactic": tactic,
            "obfuscation": obfuscation,
            "delay": delay
        }

