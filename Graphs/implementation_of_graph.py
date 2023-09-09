import queue


class Graph:
    def __init__(self, vertices):
        self.nVertices = vertices
        self.matrix = [[0]*vertices for i in range(vertices)]

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        self.matrix[v1][v2] = 0
        self.matrix[v2][v1] = 0

    def has_edge(self, v1, v2):
        return self.matrix[v1][v2] == 1

    def print_graph(self):
        x = ""
        for row in self.matrix:
            print(row)
        print()

    def graph_input(self):
        edges = int(input("No of Edges "))

        for i in range(edges):
            print("Enter edge vertices to add ")
            v1, v2 = [int(x) for x in input().split()]
            self.add_edge(v1, v2)

    def _dfs_helper(self, sv, visited):
        visited[sv] = True
        print(sv)
        for i in range(self.nVertices):
            if not visited[i] and self.matrix[sv][i] == 1:
                visited[i] = True
                self._dfs_helper(i, visited)

    def dfs(self):
        visited = [False]*self.nVertices
        self._dfs_helper(0, visited)

    def _bfs_helper(self, sv, visited):
        q = queue.Queue()
        visited[sv] = True
        q.put(sv)

        while not q.empty():
            front = q.get()
            print(front)
            for i in range(self.nVertices):
                if not visited[i] and self.matrix[front][i] == 1:
                    visited[i] = True
                    q.put(i)

    def bfs(self):
        visited = [False]*self.nVertices
        self._bfs_helper(0, visited)


G = Graph(7)
G.graph_input()
G.print_graph()
print("----------------------------")
G.dfs()
print("--------------------------------------------")
G.bfs()
