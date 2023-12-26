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

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for adjacent_vertex in self.graph:
                self.graph[adjacent_vertex] = [v for v in self.graph[adjacent_vertex] if v != vertex]

    def remove_edge(self, first_vertex, second_vertex):
        if first_vertex in self.graph and second_vertex in self.graph:
            self.graph[first_vertex] = [v for v in self.graph[first_vertex] if v != second_vertex]
            self.graph[second_vertex] = [v for v in self.graph[second_vertex] if v != first_vertex]
