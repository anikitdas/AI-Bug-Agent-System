import subprocess

def reproduce(data):
    try:
        result = subprocess.run(
            ["python", "tools/repro_script.py"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            error_lines = result.stderr.strip().split("\n")
            last_line = error_lines[-1]

            # 🔥 CLEAN IT
            clean_error = last_line.replace("Exception: Reproduced Error: ", "")

            return {
                "status": "failed",
                "script": "tools/repro_script.py",
                "error": clean_error
            }
        else:
            return {
                "status": "passed"
            }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }