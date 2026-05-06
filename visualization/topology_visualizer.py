
import pandas as pd
import networkx as nx
from pyvis.network import Network
from pathlib import Path

Path("topology").mkdir(exist_ok=True)

net = Network(
    height="750px",
    width="100%",
    bgcolor="#111111",
    font_color="white"
)

try:
    df = pd.read_csv("alerts/alerts.csv")

    unique_ips = set(df["src_ip"]).union(set(df["dst_ip"]))

    suspicious = set(
        df[df["severity"].isin(["HIGH", "CRITICAL"])]["src_ip"]
    )

    G = nx.Graph()

    for ip in unique_ips:

        color = "green"
        size = 20
        title = "Normal Device"

        if ip in suspicious:
            color = "red"
            size = 35
            title = "Suspicious Device"

        G.add_node(ip)

        net.add_node(
            ip,
            label=ip,
            color=color,
            title=title,
            size=size
        )

    for _, row in df.tail(200).iterrows():

        src = row["src_ip"]
        dst = row["dst_ip"]

        if src != dst:
            G.add_edge(src, dst)

            net.add_edge(
                src,
                dst,
                title=row["protocol"]
            )

    output = "topology/network_topology.html"

    net.save_graph(output)

    print(f"Topology generated: {output}")

except Exception as e:
    print(e)
