# BFS Function Definition
def bfs(graph, start_node):
    visited = []                # List to keep track of visited nodes
    queue = [start_node]        # Initialize the queue with the start node
    
    while queue:
        node = queue.pop(0)     # Dequeue a node
        
        if node not in visited:
            visited.append(node)  # Mark node as visited
            print(f"Traversing: {node}")
            queue.extend(graph[node])  # Add neighbors to the queue
    
    return visited

# Function to get user input for the graph
def get_graph_from_input():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    
    for _ in range(n):
        node = input("Enter the node name: ")
        neighbors = input(f"Enter neighbors of {node} separated by spaces: ").split()
        graph[node] = neighbors
    
    return graph

# Example usage
graph = get_graph_from_input()
start_node = input("Enter the starting node: ")
visited_nodes = bfs(graph, start_node)
print("BFS traversal order:", visited_nodes)
