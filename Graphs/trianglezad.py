def has_triangle(graph):
    for node in graph:
        neighbors = graph[node]
        for neighbor1 in neighbors:
            for neighbor2 in neighbors:
                if neighbor1 != neighbor2 and neighbor2 in graph.get(neighbor1, set()):
                    return "YES"
    return "NO"

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

result = has_triangle(graph)
print(result)
