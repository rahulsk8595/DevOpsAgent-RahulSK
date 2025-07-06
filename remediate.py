import os
import datetime
import subprocess

# Choose either service name or Docker container name
SERVICE_NAME = "nginx"  # You can change this to "nginx" or a Docker container

def restart_service():
    try:
        print(f"🔁 Attempting to restart service: {SERVICE_NAME}")
        result = subprocess.run(["sudo", "systemctl", "restart", SERVICE_NAME], check=True)
        print("✅ Service restarted successfully.")

        # Optionally, check status
        status = subprocess.run(["systemctl", "is-active", SERVICE_NAME], capture_output=True, text=True)
        if status.stdout.strip() == "active":
            print("🟢 Service is active and running.")
            return True
        else:
            print("❌ Service failed to start.")
            return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Error restarting service: {e}")
        return False

if __name__ == "__main__":
    success = restart_service()
    
    with open("remediation.log", "a") as log_file:
        log_file.write(f"[{datetime.datetime.now()}] Restarted {SERVICE_NAME} - Success: {success}\n")
