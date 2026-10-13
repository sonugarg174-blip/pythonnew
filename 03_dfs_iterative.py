# Program 3: Iterative Depth-First Search (DFS)
# Iterative DFS uses a stack instead of recursion.


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

    def dfs_iterative(self, start):
        if start not in self.adjacency_list:
            print(f"Vertex {start} does not exist.")
            return

        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")

                # Reverse order keeps traversal similar to the adjacency-list order
                for neighbor in reversed(self.adjacency_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")

    print("Iterative DFS traversal starting from A:")
    graph.dfs_iterative("A")
    print()
