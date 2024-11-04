def prim(graph, start_node):
    # Initialize the visited set with the starting node
    visited = set([start_node])
    
    # Initialize the list of edges with all edges from the start node
    # Each edge is represented as a tuple (weight, from_node, to_node)
    edges = [(weight, start_node, neighbor) for neighbor, weight in graph[start_node].items()]
    
    # Initialize a list to store edges in the Minimum Spanning Tree (MST)
    mst_edges = []
    
    # Initialize the total weight of the MST
    mst_weight = 0

    # Continue until there are no more edges to process
    while edges:
        # Sort edges by weight to always pick the minimum edge
        edges.sort()
        
        # Remove and get the edge with the smallest weight
        weight, frm, to = edges.pop(0)

        # Check if the destination node has not been visited
        if to not in visited:
            # Mark the destination node as visited
            visited.add(to)
            
            # Add the edge's weight to the total MST weight
            mst_weight += weight
            
            # Record the edge as part of the MST
            mst_edges.append((frm, to, weight))

            # Add all edges from the newly visited node to unvisited neighbors
            for neighbor, weight in graph[to].items():
                if neighbor not in visited:
                    edges.append((weight, to, neighbor))

    # Output the edges in the MST and return the total weight
    print("Edges in the MST:", mst_edges)
    return mst_weight

# Example usage:
# Define a sample graph with weights using an adjacency list
graph = {
    'A': {'B': 14, 'C': 3},
    'B': {'A': 14, 'C': 10, 'F': 5, 'H': 6},
    'C': {'A': 3, 'B': 10, 'D': 8},
    'D': {'C': 8, 'E': 5, 'F': 2},
    'E': {'D': 5},
    'F': {'D': 2, 'G': 9, 'H': 4, 'B': 5},
    'G': {'F': 9},
    'H': {'B': 6, 'F': 4}
}

# Define the starting node for Prim's algorithm
start_node = 'A'

# Execute the Prim's algorithm function and print the total MST weight
print("Minimum Spanning Tree Weight:", prim(graph, start_node))
