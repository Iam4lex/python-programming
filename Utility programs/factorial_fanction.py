import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Define the nodes
nodes = {
    "Head Office Router": (0, 4),
    "Branch Office Router": (6, 4),
    "Head Office Switch": (-1, 2),
    "Branch Office Switch": (7, 2),
    "Head Office Firewall": (-2, 4),
    "Internet": (3, 6),
}

# Define office devices
head_office_devices = ["Admin PC 1", "Admin PC 2", "Printer", "Access Point"]
branch_office_devices = ["Admin PC 3", "Admin PC 4"]

# Add all nodes to the graph
G.add_nodes_from(nodes)

# Add nodes for devices and connect to respective switches
for i, device in enumerate(head_office_devices):
    G.add_node(device)
    G.add_edge(device, "Head Office Switch")

for i, device in enumerate(branch_office_devices):
    G.add_node(device)
    G.add_edge(device, "Branch Office Switch")

# Connect the head office switch to head office router, and branch office switch to branch router
G.add_edge("Head Office Switch", "Head Office Router")
G.add_edge("Branch Office Switch", "Branch Office Router")

# Connect head office router to firewall and firewall to internet
G.add_edge("Head Office Router", "Head Office Firewall")
G.add_edge("Head Office Firewall", "Internet")

# VPN connection from head office to branch office router
G.add_edge("Head Office Router", "Branch Office Router", color="blue", style="dashed")

# Position the main elements and devices around them
pos = nx.spring_layout(G)
pos.update(nodes)

# Draw the nodes and edges
plt.figure(figsize=(10, 8))
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=2000)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrows=True, arrowstyle="-|>", edge_color="black")

# Add legend and title
plt.title("Hybrid Network Topology")
plt.axis("off")
plt.show()
