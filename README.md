# 🤖 DevOpsAgent – Rahul SK

An AI-powered multi-tool DevOps agent for automated monitoring, anomaly detection, root cause analysis, and auto-remediation — designed using Prometheus, Python, and LLMs.

---

## 🔧 Key Features

- 🧠 Detects CPU spikes using Prometheus + Node Exporter
- 🔍 Analyzes logs with OpenAI (or mock fallback)
- 🔁 Auto-remediates by restarting nginx service
- 📣 Sends alerts to Slack with detailed incident reports
- 🛡️ Includes cooldown logic to avoid alert spam
- ✅ Designed to run on Free-Tier EC2 instances

---

## 📁 Project Structure

| File             | Purpose                                               |
|------------------|-------------------------------------------------------|
| `monitor.py`     | Agent loop for monitoring, detection, triggering      |
| `analyze.py`     | Log analyzer using OpenAI API (mocked if quota hit)   |
| `remediate.py`   | Restarts nginx service if required                    |
| `notify.py`      | Slack notification sender                             |
| `requirements.txt` | Required Python dependencies                        |
| `.env` (or env vars) | API keys for OpenAI, Slack                        |
| `README.md`      | Documentation                                         |

---

## 🔧 1. Setup EC2 + Prometheus + Node Exporter + Python Agent

### ☁️ Launch AWS EC2 (Ubuntu 22.04, t2.micro)
```bash
# Use AWS Console or CLI to launch an EC2 instance (t2.micro)
# SSH into it
ssh -i <your-key.pem> ubuntu@<your-ec2-public-ip>

##🛠️ Install Prometheus
cd /opt
wget https://github.com/prometheus/prometheus/releases/download/v2.52.0/prometheus-2.52.0.linux-amd64.tar.gz
tar -xvzf prometheus-2.52.0.linux-amd64.tar.gz
mv prometheus-2.52.0.linux-amd64 prometheus
cd prometheus

##Create prometheus.yml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']

##Start Prometheus
./prometheus --config.file=prometheus.yml > prometheus.log 2>&1 &

##📦 Install Node Exporter
cd /opt
wget https://github.com/prometheus/node_exporter/releases/download/v1.9.1/node_exporter-1.9.1.linux-amd64.tar.gz
tar -xvf node_exporter-1.9.1.linux-amd64.tar.gz
cd node_exporter-1.9.1.linux-amd64
./node_exporter > node_exporter.log 2>&1 &

##Clone Project and Setup Python
cd ~
git clone https://github.com/rahulsk8595/DevOpsAgent-RahulSK.git
cd DevOpsAgent-RahulSK
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

##Configure Environment Variables
nano .env
OPENAI_API_KEY=sk-xxxxxxxxxxxx
SLACK_TOKEN=xoxb-xxxxxxxxxxxxx
SLACK_CHANNEL_ID=C0944JDF2R5


##▶️ Run the Monitoring Agent
cd ~/DevOpsAgent-RahulSK
source venv/bin/activate
python monitor.py

##💥 2. Simulate CPU Spike (for testing)
yes > /dev/null &

#Stop it later
pkill yes

##🧪 Sample Output (Slack Notification)
🚨 CPU Spike Detected!
🧠 Root Cause: Infinite loop suspected
🔁 Action: Restarted nginx
🟢 Status: Resolved

##🧪 Testing Checklist
| Component                | Status |
| ------------------------ | ------ |
| Node Exporter Running    | ✅      |
| Prometheus Running       | ✅      |
| CPU Spike Detection      | ✅      |
| Log Analysis (Mock/Real) | ✅      |
| nginx Auto-Restart       | ✅      |
| Slack Notification       | ✅      |

🧠 Agent Personality
You are OpsBot – vigilant, transparent, and action-driven.

Constantly monitors metrics

Confidently remediates when safe

Avoids spam with cooldown logic

Notifies team with clarity and precision

##👨‍💻 Author
Rahul SK
📧 rahulsk8595@gmail.com
🔗 GitHub: rahulsk8595


