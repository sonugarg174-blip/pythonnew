"""Bellman-Ford: shortest paths with negative edges allowed."""

def bellman_ford(vertices, edges, source):
    distance = {vertex: float("inf") for vertex in vertices}
    previous = {vertex: None for vertex in vertices}
    distance[source] = 0

    # A shortest simple path uses at most |V| - 1 edges.
    for _ in range(len(vertices) - 1):
        changed = False
        for start, end, weight in edges:
            if distance[start] != float("inf"):
                candidate = distance[start] + weight
                if candidate < distance[end]:
                    distance[end] = candidate
                    previous[end] = start
                    changed = True
        if not changed:
            break

    # One more successful relaxation means a negative cycle exists.
    for start, end, weight in edges:
        if distance[start] != float("inf") and distance[start] + weight < distance[end]:
            return distance, previous, True

    return distance, previous, False


vertices = ["A", "B", "C", "D"]
edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "C", -2),
    ("C", "D", 3),
    ("B", "D", 4)
]

distances, previous, negative_cycle = bellman_ford(vertices, edges, "A")

if negative_cycle:
    print("A negative-weight cycle exists.")
else:
    print("Shortest distances from A:")
    for vertex in vertices:
        print(vertex, ":", distances[vertex])
