class Grafo:
    def __init__(self, num_vertices, direcionado):
        self.num_vertices = num_vertices
        self.lista_adj = [[] for _ in range(num_vertices)]
        self.pre = [0]*num_vertices
        self.pos = [0]*num_vertices
        self.direcionado = direcionado

    def adiciona_aresta(self, origem, destino):
        self.lista_adj[origem].append(destino)
        if not self.direcionado:
            self.lista_adj[destino].append(origem)

    def dfs(self, vertice, visitado, componente=None, pilha=None):
        global tempo
        visitado[vertice] = True
        tempo += 1
        self.pre[vertice] = tempo
        
        if componente is not None:
            componente.append(vertice)
        
        for vizinho in self.lista_adj[vertice]:
            if not visitado[vizinho]:
                self.dfs(vizinho, visitado, componente, pilha)
        
        tempo += 1
        self.pos[vertice] = tempo
        
        if self.direcionado and pilha is not None:
            pilha.insert(0, vertice)

    def encontra_componentes(self):
        visitado = [False]*self.num_vertices
        componentes = []
        pilha = [] if self.direcionado else None
        for vertice in range(self.num_vertices):
            if not visitado[vertice]:
                componente = []
                self.dfs(vertice, visitado, componente, pilha)
                componentes.append(componente)
        return componentes, pilha
        
    def exibe(self):
        for i, adj in enumerate(self.lista_adj):
            print(f"{i}: {' -> '.join(map(str, adj))}")

    def exibe_pre_pos(self):
        print("\nTempo de visita da pré e pós-ordem:")
        for i in range(self.num_vertices):
            print(f"Vértice {i} ({self.pre[i]}/{self.pos[i]})")
    

# Teste
tempo = 0
num_vertices = 4
direcionado = False;


contador = 0;
grafo = Grafo(num_vertices, direcionado);

grafo.adiciona_aresta(1, 3)
grafo.adiciona_aresta(2, 0)
grafo.adiciona_aresta(3, 1)
grafo.adiciona_aresta(0, 2)
print("Lista de vizinhança do grafo:")
grafo.exibe()
print("\nBusca DFS no grafo:")
componentes, pilha = grafo.encontra_componentes()
grafo.exibe_pre_pos()

if len(componentes) > 1:
    print(f"\nForam encontrados {len(componentes)} componentes desconexos no grafo:\n", componentes)
else:
    print("\nNão foram encontrados componentes desconexos no grafo:\n", componentes)
if direcionado:
    print("\nOrdem topológica do grafo: \n" if len(pilha) > 1 else "\nNão existe uma ordem topológica para o grafo:", list(pilha))

