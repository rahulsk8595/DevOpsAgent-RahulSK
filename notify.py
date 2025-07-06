import os
import requests
import datetime

# Slack credentials (use ENV VARs in production)
SLACK_TOKEN = "xoxb-2657988558930-9155453330996-VI1Kpm3QgepbeyA0phzAYFxN"
SLACK_CHANNEL_ID = "C0944JDF2R5"

def send_slack_notification(cpu_usage, root_cause, action_taken, service_status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = (
        "*🚨 CPU Spike Detected*\n"
        f"*🧠 Root Cause:* {root_cause}\n"
        f"*🔁 Action Taken:* {action_taken}\n"
        f"*✅ Current Status:* {service_status}\n"
        f"*📅 Timestamp:* {timestamp}"
    )

    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "channel": SLACK_CHANNEL_ID,
            "text": message
        }
    )

    if response.ok and response.json().get("ok"):
        print("📤 Slack notification sent successfully.")
    else:
        print("❌ Failed to send Slack message:", response.text)

# Test this independently
if __name__ == "__main__":
    # Simulated values for testing
    send_slack_notification(
        cpu_usage="100%",
        root_cause="Infinite loop in app process",
        action_taken="Restarted nginx",
        service_status="nginx is active"
    )
