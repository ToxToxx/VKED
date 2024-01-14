def min_transfers(graph, start, end):
    visited = set()
    queue = [(start, 0)]  # Используем список для очереди, каждый элемент - кортеж (станция, количество пересадок)

    while queue:
        current_station, transfers = queue.pop(0)
        visited.add(current_station)

        if current_station == end:
            return transfers - 1

        for neighbor_station in graph.get(current_station, []):
            if neighbor_station not in visited:
                queue.append((neighbor_station, transfers + 1))

    return "No path found"

# Ввод данных
N = int(input())
graph = {}

for _ in range(N):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

start, end = map(int, input().split())

# Вызов функции и вывод результата
result = min_transfers(graph, start, end)
print(result)
