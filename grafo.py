import networkx as nx
import matplotlib.pyplot as plt


class GrafoNaoDirecionado:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz_adj = [[0] * vertices for _ in range(vertices)]

    def adicionar_aresta(self, u, v):
        self.matriz_adj[u][v] = 1
        self.matriz_adj[v][u] = 1

    def mostrar_matriz_adjacencia(self):
        print("Matriz de Adjacência:")
        for linha in self.matriz_adj:
            print(linha)

    def mostrar_grafo(self):
        print("Disposição do Grafo:")
        for i in range(self.vertices):
            vizinhos = []
            for j in range(self.vertices):
                if self.matriz_adj[i][j] == 1:
                    vizinhos.append(j)
            print(f"Vértice {i}: {vizinhos}")

    def plotar_grafo(self):
        G = nx.Graph()
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                if self.matriz_adj[i][j] == 1:
                    G.add_edge(i, j)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()


# Exemplo de uso:
num_vertices = int(input("Digite o número de vértices do grafo não direcionado: "))
grafo_nd = GrafoNaoDirecionado(num_vertices)

for i in range(num_vertices):
    u, v = map(int, input(f"Digite a aresta {i + 1} (formato: u v): ").split())
    grafo_nd.adicionar_aresta(u, v)

grafo_nd.mostrar_matriz_adjacencia()
grafo_nd.mostrar_grafo()
grafo_nd.plotar_grafo()
