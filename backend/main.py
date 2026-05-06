
from fastapi import FastAPI
import pandas as pd
import psutil

app = FastAPI(title="NetSentinelX")

@app.get("/")
def root():
    return {"message": "NetSentinelX API Running"}

@app.get("/stats")
def stats():
    net = psutil.net_io_counters()

    return {
        "bytes_sent": net.bytes_sent,
        "bytes_recv": net.bytes_recv,
        "packets_sent": net.packets_sent,
        "packets_recv": net.packets_recv
    }

@app.get("/alerts")
def alerts():
    try:
        df = pd.read_csv("alerts/alerts.csv")
        return df.tail(50).to_dict(orient="records")
    except:
        return []
