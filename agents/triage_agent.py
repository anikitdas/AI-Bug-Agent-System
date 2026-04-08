def triage(bug_report):
    lines = bug_report.split("\n")
    return {
        "summary": lines[0],
        "details": bug_report,
        "severity": "medium"
    }