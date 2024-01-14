def dijkstra(graph, start, end):
    infinity = float('inf')
    shortest_paths = {vertex: (infinity, None) for vertex in graph}
    shortest_paths[start] = (0, None)
    current_vertex = start
    visited = set()

    while current_vertex != end:
        visited.add(current_vertex)
        destinations = graph[current_vertex]
        weight_to_current_vertex = shortest_paths[current_vertex][0]

        for next_vertex, weight in destinations.items():
            weight_to_neighbour = weight_to_current_vertex + weight
            if weight_to_neighbour < shortest_paths[next_vertex][0]:
                shortest_paths[next_vertex] = (weight_to_neighbour, current_vertex)

        next_destinations = {vertex: shortest_paths[vertex] for vertex in shortest_paths if vertex not in visited}
        if not next_destinations:
            break

        current_vertex = min(next_destinations, key=lambda k: next_destinations[k][0])

    path, current_vertex = [], end
    while current_vertex is not None:
        path.append(current_vertex)
        next_vertex = shortest_paths[current_vertex][1]
        current_vertex = next_vertex
    path = path[::-1]

    return path, shortest_paths[end][0]

N = int(input())
graph = {}

for _ in range(N):
    u, v, weight = map(int, input().split())
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = weight
    graph[v][u] = weight

start, end = map(int, input().split())

path, shortest_distance = dijkstra(graph, start, end)
print(shortest_distance)