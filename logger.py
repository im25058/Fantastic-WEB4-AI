import json
import time


class AuditLogger:

    def __init__(self):

        self.logs = []


    def log(self, step, action, input_data, output_data):

        entry = {

            "step": step,
            "action": action,
            "input": input_data,
            "output": output_data,
            "timestamp": time.time()

        }

        self.logs.append(entry)


    def save_logs(self):

        with open("audit_logs.json", "w") as f:

            json.dump(self.logs, f, indent=4)

        return self.logs