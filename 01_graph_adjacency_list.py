# Program 1: Implement a Graph using an Adjacency List

class Graph:
    def __init__(self):
        # Dictionary: each vertex maps to a list of its neighboring vertices
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add vertices automatically if they do not exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Undirected graph: add the edge in both directions
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def display(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {neighbors}")


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_edge("C", "E")

    print("Graph represented using an adjacency list:")
    graph.display()
