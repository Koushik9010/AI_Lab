def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start + " " , end="")

    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

if __name__ == "__main__":
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node}: ").strip().split()
        graph[node] = set(n.strip() for n in neighbors)

    start_node = input("Enter the start node: ").strip()
    print("Following is DFS traversal: ")
    dfs(graph, start_node)