
# NetSentinelX Ultimate

Intelligent Network Threat Detection & SOC Monitoring Platform

## Features
- Real-time packet sniffing
- SYN flood detection
- Port scan detection
- ICMP flood detection
- Threat intelligence scoring
- Streamlit SOC dashboard
- FastAPI backend
- Interactive network topology visualization
- Attack simulators
- Device scanning
- Alert analytics

## Installation

pip install -r requirements.txt

## Run

Backend:
uvicorn backend.main:app --reload

Threat Engine:
python monitoring/sniffer.py

Dashboard:
streamlit run dashboard/app.py

Topology:
python visualization/topology_visualizer.py

Simulators:
python simulator/scan_simulator.py
python simulator/ddos_simulator.py
