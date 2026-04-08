from agents.triage_agent import triage
from agents.log_agent import analyze_logs
from agents.repro_agent import reproduce
from agents.fix_agent import fix_plan
from agents.critic_agent import critic
import json
import os

def main():
    print("🚀 Running Multi-Agent Bug System...\n")

    # Read inputs
    with open("data/bug_report.txt") as f:
        bug = f.read()

    with open("data/logs.txt") as f:
        logs = f.read()

    # Agents execution
    triage_data = triage(bug)
    print("🔍 Triage:", triage_data)

    log_data = analyze_logs(logs)
    print("📜 Logs:", log_data)

    repro = reproduce(triage_data)
    print("🧪 Repro:", repro)

    fix = fix_plan(triage_data, log_data, repro)
    print("🛠 Fix:", fix)

    review = critic(fix)
    print("🧠 Review:", review)

    # ✅ FIX: ensure output folder exists
    os.makedirs("output", exist_ok=True)

    # Final structured output
    final_output = {
        "bug_summary": triage_data,
        "evidence": log_data,
        "reproduction": repro,
        "fix_plan": review
    }

    # Save JSON
    with open("output/result.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("\n✅ Output saved to output/result.json")

if __name__ == "__main__":
    main()