class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def bellman_ford(edges, num_vertices, source):
    distance = [float('inf')] * num_vertices
    distance[source] = 0

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        for edge in edges:
            if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.destination]:
                distance[edge.destination] = distance[edge.source] + edge.weight

    # Check for negative cycles
    for edge in edges:
        if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.destination]:
            print("Граф содержит отрицательный цикл")
            return

    # Print the shortest distances
    for i in range(num_vertices):
        print(f"Вершина: {i + 1}, Расстояние: {'бесконечность' if distance[i] == float('inf') else distance[i]}")

if __name__ == "__main__":
    num_edges = int(input())
    edges = []

    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        edges.append(Edge(u - 1, v - 1, weight))

    source = int(input())

    bellman_ford(edges, max(max(e.source, e.destination) for e in edges) + 1, source - 1)
