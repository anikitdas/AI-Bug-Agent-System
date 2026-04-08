import re

def analyze_logs(logs):
    errors = re.findall(r'Error: (.*)', logs)
    stack = re.findall(r'at (.*)', logs)

    return {
        "error": errors[0] if errors else "No error found",
        "stack_trace": stack,
        "raw_sample": logs[:200]
    }