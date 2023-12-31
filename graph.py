import queue
class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]

    def print(self):
        print(f"Matriz: \n{self.matrix}\n")
        print(f'Lista de adjacência: {self.list}\n')
        
    def bfs(self, s, t):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        visitados = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(s)
        visitados[s] = True
        dist[s] = 0
        caminho = []
        v2 = t
        
        while Q.empty() != True:
            p = Q.get()
            print("Vértice: " + str(p))
            if p == t:
              break
            
            for v in self.list[p]:
                if visitados[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    visitados[v] = True
                  
        if dist[t] == -1:
          print("Não há caminho.")
        else:
          while t != -1:
            caminho.append(t)
            t = ant[t]
          print(f"Caminho inverso do início {s} até o final {v2}: {caminho}")
          caminho.reverse()
          print(f"Caminho do início {s} até o final {v2}: {caminho}")
          

      
        return visitados, caminho
      
    def dfs(self, source):
        visitados = [False for _ in range(self.num_vertices)]
        pilha = []
        pilha.append(source)
        caminho = []

        while pilha:
            u = pilha.pop()
            if not visitados[u]:
                visitados[u] = True
                caminho.append(u)
                print(f"Vértice: {u}")
                for v in self.list[u]:
                      if not visitados[v]:
                        pilha.append(v)
                
        return visitados, caminho

