
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(layout="wide")

st.title("🛡️ NetSentinelX SOC Dashboard")

try:
    stats = requests.get("http://127.0.0.1:8000/stats").json()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Bytes Sent", stats["bytes_sent"])
    c2.metric("Bytes Received", stats["bytes_recv"])
    c3.metric("Packets Sent", stats["packets_sent"])
    c4.metric("Packets Received", stats["packets_recv"])

except:
    st.warning("Backend not running.")

try:
    df = pd.read_csv("alerts/alerts.csv")

    st.subheader("Threat Alerts")

    severity = st.selectbox(
        "Filter Severity",
        ["ALL", "LOW", "MEDIUM", "HIGH", "CRITICAL"]
    )

    filtered = df

    if severity != "ALL":
        filtered = df[df["severity"] == severity]

    st.dataframe(filtered.tail(50), use_container_width=True)

    st.subheader("Threat Distribution")

    fig1 = px.histogram(filtered, x="alert")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Protocol Distribution")

    fig2 = px.pie(filtered, names="protocol")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Top Suspicious IPs")

    top_ips = filtered["src_ip"].value_counts().head(10)

    fig3 = px.bar(
        x=top_ips.index,
        y=top_ips.values
    )

    st.plotly_chart(fig3, use_container_width=True)

except Exception as e:
    st.info(f"Waiting for traffic data... {e}")
