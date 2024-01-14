class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def bellman_ford(edges, num_vertices):
    distance = [float('inf')] * num_vertices
    distance[0] = 0

    # Релаксация рёбер несколько раз
    for _ in range(num_vertices - 1):
        for edge in edges:
            if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.destination]:
                distance[edge.destination] = distance[edge.source] + edge.weight

    # Проверка наличия отрицательных циклов
    for edge in edges:
        if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.destination]:
            return {"error": "Граф содержит отрицательный цикл"}

    # Формирование результата
    result = {}
    for i in range(num_vertices):
        result[i + 1] = distance[i] if distance[i] != float('inf') else 'бесконечность'

    return result

if __name__ == "__main__":
    # Ввод количества рёбер
    num_edges = int(input())
    edges = []

    max_vertex = 0  # Используем переменную для хранения максимального номера вершины

    # Ввод рёбер и создание объектов класса Edge
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        edges.append(Edge(u - 1, v - 1, weight))
        
        # Обновляем максимальный номер вершины
        max_vertex = max(max_vertex, u, v)

    # Вызов функции Беллмана-Форда и вывод результата
    result = bellman_ford(edges, max_vertex + 1)
    
    if "error" in result:
        print(result["error"])
    else:
        for vertex, distance in result.items():
            print(f"Вершина: {vertex}, Расстояние: {distance}")
