# Depth-First Search (DFS) Function Definition
def dfs(graph, node, visited=None):
    # Initialize the visited set if it's not provided (for first call)
    if visited is None:
        visited = set()
    
    # Mark the current node as visited by adding it to the visited set
    visited.add(node)
    print(f"Visiting: {node}")
    
    # Recursively visit all unvisited neighbors of the current node
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    # Return the set of visited nodes after completing DFS traversal
    return visited

# Example usage:
# Define a sample graph using an adjacency list
graph = {
    0: [1, 4],
    1: [2],
    2: [0],
    3: [2],
    4: [3]
}

# Define the starting node for DFS traversal
start_node = 0

# Execute the DFS function and print the result
visited_nodes = dfs(graph, start_node)

# Final Output
print("DFS complete. Visited nodes:", visited_nodes)
