import networkx as nx
import matplotlib.pyplot as plt
# Define the graph using the given weights
weights = [
    [0, 10, 15, 10],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [10, 25, 30, 0]
]

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(range(len(weights)))

# Add edges with weights
for i in range(len(weights)):
    for j in range(i+1, len(weights[i])):
        G.add_edge(i, j, weight=weights[i][j])
        G.add_edge(j, i, weight=weights[i][j])

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='k', linewidths=1, font_size=15)

# Add edge labels with weights
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Weighted Graph Visualization")
plt.show()