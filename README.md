# 🚀 AI Bug Analyzer

This is a simple project that helps find and understand bugs using multiple small agents.

---

## 📌 What it does

* Takes a bug report and logs
* Finds the error from logs
* Runs a script to reproduce the bug
* Shows why the error happened
* Suggests how to fix it
* Saves output in a JSON file

---

## 🧠 Agents used

* Triage → reads the bug
* Log → finds error
* Repro → runs script
* Fix → gives solution
* Critic → checks solution

---

## ⚙️ How to run

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## 📂 Output

Check this file after running:

```
output/result.json
```

---

## 🧪 Note

The script is made to fail on purpose
so the system can detect the bug properly.


