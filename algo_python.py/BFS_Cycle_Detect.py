def bfs_cycle_detection(graph, start_node):
    # Initialize an empty list to keep track of visited nodes
    visited = []
    
    # Initialize the queue with the start node and a parent reference (None for start node)
    # Each element in the queue is a tuple (node, parent)
    queue = [(start_node, None)]
    
    # Loop until there are no more nodes to process in the queue
    while queue:
        # Remove and retrieve the first element in the queue
        node, parent = queue.pop(0)
        
        # Check if the node has not been visited yet
        if node not in visited:
            # Add the node to the list of visited nodes
            visited.append(node)
            
            # Print the current node as it's being traversed
            print(f"Traversing: {node}")
            
            # Iterate over each neighboring node (connected node)
            for neighbor in graph[node]:
                # If the neighbor has not been visited, add it to the queue with the current node as its parent
                if neighbor not in visited:
                    queue.append((neighbor, node))
                # If the neighbor has already been visited and is not the parent, a cycle is detected
                elif neighbor != parent:
                    # Print cycle detection information
                    print(f"Cycle detected between {node} and {neighbor}")
                    return True  # Return True to indicate a cycle was found
    
    # If the entire graph is traversed without detecting a cycle, return False
    return False

# Example usage:
# Define a sample graph using an adjacency list
graph = {
    0: [1, 4],
    1: [2],
    2: [0],
    3: [2],
    4: [3]
}

# Define the starting node for BFS traversal
start_node = 0

# Execute the BFS cycle detection function and print the result
has_cycle = bfs_cycle_detection(graph, start_node)
print("Cycle exists:" if has_cycle else "No cycle detected.")
