import time
import datetime
import os
from prometheus_api_client import PrometheusConnect

# Initialize Prometheus connection
prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)

def get_cpu_usage():
    # MOCKING HIGH CPU USAGE FOR TESTING
    print(f"[{datetime.datetime.now()}] (Mocked) CPU Usage: 100.0%")
    return 100.0

    # Uncomment this for real Prometheus metric
    # metric_data = prom.get_current_metric_value("node_cpu_seconds_total")
    # Process and return actual usage % here

def monitor_loop():
    print("📡 Monitoring CPU Usage...")

    breach_threshold = 80.0  # Trigger threshold
    breach_duration = 10     # Duration in seconds to qualify as spike
    breach_start = None

    while True:
        usage = get_cpu_usage()
        print(f"[{datetime.datetime.now()}] CPU Usage: {usage}%")

        if usage > breach_threshold:
            if breach_start is None:
                breach_start = time.time()
            elif time.time() - breach_start >= breach_duration:
                print("🚨 CPU Spike Detected!")
                print("🔍 Triggering log analysis...")

                # Step 1: Analyze logs
                os.system("python3 analyze.py > analysis.txt")

                # Step 2: Read LLM result
                with open("analysis.txt") as f:
                    analysis_result = f.read().split("🧠 [MOCK] Root Cause Analysis from LLM:")[-1].strip()

                # Step 3: Remediate
                os.system("python3 remediate.py > remediation.log")

                # Step 4: Check if successful
                with open("remediation.log") as f:
                    last_line = f.readlines()[-1]
                    service_status = "active" if "Success" in last_line else "failed"

                # Step 5: Notify
                from notify import send_slack_notification
                send_slack_notification(
                    cpu_usage=f"{usage}%",
                    root_cause=analysis_result,
                    action_taken="Restarted nginx",
                    service_status=f"nginx is {service_status}"
                )

                breach_start = None  # Reset
        else:
            breach_start = None  # Reset if no longer breaching

        time.sleep(5)  # Poll every 5 seconds

# Run monitor
monitor_loop()
