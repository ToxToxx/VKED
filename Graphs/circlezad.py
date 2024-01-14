def dfs(graph, node, visited, current_circle):
    visited[node] = True
    current_circle.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, current_circle)

def count_social_circles(graph):
    visited = {node: False for node in graph}
    social_circles = []

    for node in graph:
        if not visited[node]:
            current_circle = []
            dfs(graph, node, visited, current_circle)
            social_circles.append(set(current_circle))

    return len(social_circles)

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n)]

graph = {}
for edge in edges:
    a, b = edge
    if a not in graph:
        graph[a] = set()
    if b not in graph:
        graph[b] = set()
    graph[a].add(b)
    graph[b].add(a)

result = count_social_circles(graph)
print(result)
