# 🤖 DevOpsAgent – Rahul SK

AI-powered multi-tool DevOps agent for automated infrastructure monitoring, anomaly detection, root cause analysis, and remediation.

---

## 🔧 Features

- 🧠 Detects CPU spikes using Prometheus metrics
- 🔍 Analyzes system logs using OpenAI (mocked)
- 🔁 Automatically remediates by restarting `nginx`
- 📣 Sends alerts to Slack with summary and status
- 🛡️ Cooldown logic to prevent repeated alerts

---

## 📁 Project Structure

| File | Purpose |
|------|---------|
| `monitor.py` | Main agent loop (monitor → detect → respond) |
| `analyze.py` | Mock LLM log analyzer |
| `remediate.py` | Restarts `nginx` if issue found |
| `notify.py` | Sends Slack notification |
| `requirements.txt` | Python packages needed |
| `.env` | (Optional) for secrets like `OPENAI_API_KEY` |

---

## 🚀 How to Run

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
