class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, first_vertex, second_vertex):
        self.add_vertex(first_vertex)
        self.add_vertex(second_vertex)
        self.graph[first_vertex].append(second_vertex)
        self.graph[second_vertex].append(first_vertex)