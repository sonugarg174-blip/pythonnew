# Program 2: Breadth-First Search (BFS)
# BFS visits nearby vertices first. It uses a queue.

from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list.setdefault(vertex1, [])
        self.adjacency_list.setdefault(vertex2, [])

        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def bfs(self, start):
        if start not in self.adjacency_list:
            print(f"Vertex {start} does not exist.")
            return

        visited = {start}
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")

    print("BFS traversal starting from A:")
    graph.bfs("A")
    print()
