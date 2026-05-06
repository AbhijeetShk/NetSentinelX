import subprocess
import time
import webbrowser

processes = []

print("[1] Starting FastAPI Backend...")
backend = subprocess.Popen(
    ["uvicorn", "backend.main:app", "--reload"]
)
processes.append(backend)

time.sleep(3)

print("[2] Starting Threat Detection Engine...")
sniffer = subprocess.Popen(
    ["python", "monitoring/sniffer.py"]
)
processes.append(sniffer)

time.sleep(3)

print("[3] Starting Streamlit Dashboard...")
dashboard = subprocess.Popen(
    ["streamlit", "run", "dashboard/app.py"]
)
processes.append(dashboard)

time.sleep(5)

print("[4] Opening Dashboard...")
webbrowser.open("http://localhost:8501")

print("\\n NetSentinelX Fully Running")
print("Press CTRL+C to stop all services.")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:

    print("\\nStopping all services...")

    for p in processes:
        p.terminate()

    print("Shutdown complete.")