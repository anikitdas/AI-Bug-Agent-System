def fix_plan(triage, logs, repro):
    return {
        "root_cause": "User object is None causing attribute error",
        "patch_plan": "Add null check before calling methods on user",
        "files_affected": ["tools/repro_script.py"],
        "validation": [
            "Add unit test for null user",
            "Run reproduction script again"
        ],
        "confidence": "high"
    }