import numpy as np
import sys
import networkx as nx
import matplotlib.pyplot as plt

class FloydWarshallAlgo:
    def __init__(self, graph):
        self.graph = graph

    def floyd_warshall(self):
        V = len(self.graph)
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.graph))

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        self.print_solution(dist)
        return dist

    @staticmethod
    def print_solution(dist):
        V = len(dist)
        print("Following matrix shows the shortest distances between every pair of vertices")
        for i in range(V):
            for j in range(V):
                if dist[i][j] == float('Inf'):
                    print("%7s" % ("INF"), end=" ")
                else:
                    print("%7d" % (dist[i][j]), end=" ")
                if j == V - 1:
                    print()

class Djikstra:
    V = 10

    def minDistance(self, dist, sptSet):
        min_val = float('inf')
        min_index = -1
        for v in range(self.V):
            if sptSet[v] == False and dist[v] <= min_val:
                min_val = dist[v]
                min_index = v
        return min_index

    def getMinDistance(self, dist, destination):
        return dist[destination]

    def printSolution(self, dist, source, names):
        sourceName = names[source]
        print("Vertex Name \t\t Distance from", sourceName)
        for i in range(self.V):
            if dist[i] > 0 or i == source:
                print(names[i], "\t\t", dist[i])

    def dijkstra(self, graph, src):
        dist = [float('inf')] * self.V
        sptSet = [False] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if not sptSet[v] and graph[u][v] != 0 and dist[u] != float('inf') and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
        return dist

    @staticmethod
    def setDestLocation(user_destination_location):
        global destination_location
        destination_location = user_destination_location
        final_dist = Djikstra().getMinDistance(output_dist, destination_location)
        return final_dist

    @staticmethod
    def visualizeGraph(graph, names, shortest_path=None):
        G = nx.Graph()
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] != 0:
                    G.add_edge(names[i], names[j], weight=graph[i][j])

        pos = nx.spring_layout(G)  # positions for all nodes

        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(G, pos, width=2)

        # labels
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

        # edge labels
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Highlight shortest path, if provided
        if shortest_path:
            edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=4,node_color='red', node_size=500)
            
        plt.axis("off")
        plt.show()

def main():
    while True:
        print("Choose an algorithm:")
        print("1. Dijkstra's Algorithm")
        print("2. Floyd-Warshall Algorithm")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            run_dijkstra()
        elif choice == '2':
            run_floyd_warshall()
        elif choice == '3':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please choose again.")

def run_dijkstra():
    names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    graph = [
        [0, 3, 0, 0, 1, 0, 0, 0, 0, 0],
        [3, 0, 1, 0, 0, 0, 0, 2, 0, 0],
        [0, 1, 0, 2, 0, 0, 0, 5, 2, 0],
        [0, 0, 2, 0, 2, 0, 1, 0, 0, 3],
        [1, 0, 0, 2, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 5, 0, 0, 0],
        [0, 0, 0, 1, 0, 5, 0, 0, 0, 0],
        [0, 2, 5, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 2, 0, 0, 0, 0, 3, 0, 1],
        [0, 0, 0, 3, 0, 0, 0, 0, 1, 0]
    ]

    t = Djikstra()

    print("Enter the source location: ")
    source = int(input()) - 1

    try:
        if 0 <= source < len(graph):
            print("VALID SOURCE LOCATION")
            output_dist = t.dijkstra(graph, source)
            t.printSolution(output_dist, source, names)
            t.visualizeGraph(graph, names)
        else:
            raise Exception("Invalid source location")
    except Exception as e:
        print(e)

def run_floyd_warshall():
      #       10
      #  (0)------->(3)
      #   |         /|\
      # 5 |          |
      #   |          | 1
      #  \|/         |
      #  (1)------->(2)
      #       3
    graph = [
        [0, 5, float('Inf'), 10],
        [float('Inf'), 0, 3, float('Inf')],
        [float('Inf'), float('Inf'), 0, 1],
        [float('Inf'), float('Inf'), float('Inf'), 0]
    ]
    g = FloydWarshallAlgo(graph)
    distances = g.floyd_warshall()

if __name__ == "__main__":
    main()
