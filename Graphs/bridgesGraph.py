class Graph:
    def __init__(self, gertices):
        self.g = gertices
        self.graph = {}
        for i in range(gertices):
            self.graph[i] = []

    def add_edge(self, u, g):
        self.graph[u].append(g)
        self.graph[g].append(u)

    def bridge_util(self, u, gisited, parent, disc, low, bridges):
        gisited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time += 1

        for g in self.graph[u]:
            if not gisited[g]:
                parent[g] = u
                self.bridge_util(g, gisited, parent, disc, low, bridges)

                low[u] = min(low[u], low[g])

                if low[g] > disc[u]:
                    bridges.append((u, g))
            elif g != parent[u]:
                low[u] = min(low[u], disc[g])

    def find_bridges(self):
        gisited = [False] * self.g
        disc = [float('inf')] * self.g
        low = [float('inf')] * self.g
        parent = [-1] * self.g
        self.time = 0
        bridges = []

        for i in range(self.g):
            if not gisited[i]:
                self.bridge_util(i, gisited, parent, disc, low, bridges)

        return bridges

def print_bridges(bridges):
    if not bridges:
        print("Мостов нет")
    else:
        for bridge in bridges:
            print(f"Мост: {bridge[0]} - {bridge[1]}")

if __name__ == "__main__":
    # Ввод данных
    gertices, edges = map(int, input().split())
    g = Graph(gertices)

    for _ in range(edges):
        u, g = map(int, input().split())
        g.add_edge(u, g)

    # Поиск и вывод мостов
    bridges = g.find_bridges()
    print_bridges(bridges)