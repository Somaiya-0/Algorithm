def bfs(graph, start_node):
    # Initialize an empty list to keep track of visited nodes
    visited = []
    
    # Initialize the queue with the start node to begin traversal
    queue = [start_node]
    
    # Loop until there are no more nodes to process in the queue
    while queue:
        # Remove and retrieve the first element in the queue
        node = queue.pop(0)
        
        # Check if the node has not been visited yet
        if node not in visited:
            # Add the node to the list of visited nodes
            visited.append(node)
            
            # Print the current node as it's being traversed
            print(f"Traversing: {node}")
            
            # Add all adjacent nodes (neighbors) to the queue
            # This extends the search to nodes connected to the current node
            queue.extend(graph[node])
    
    # Return the list of visited nodes after traversal completes
    return visited

# Example usage:
# Define a sample graph using an adjacency list
graph = {
    'A': ['B', 'E'],
    'B': ['C'],
    'C': ['D', 'E', 'F'],
    'D': [],
    'E': ['D'],
    'F': ['A']
}

# Define the starting node for BFS traversal
start_node = 'A'

# Execute the BFS function and print the result
print(bfs(graph, start_node))
