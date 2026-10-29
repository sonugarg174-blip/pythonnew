"""Dijkstra's algorithm: shortest paths from one source.
Works only when all edge weights are non-negative.
"""

def dijkstra(graph, start):
    distance = {vertex: float("inf") for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distance[start] = 0
    unvisited = set(graph)

    while unvisited:
        # Pick the unvisited vertex with the smallest known distance.
        current = min(unvisited, key=lambda vertex: distance[vertex])

        if distance[current] == float("inf"):
            break  # Remaining vertices cannot be reached.

        unvisited.remove(current)

        for neighbour, weight in graph[current]:
            new_distance = distance[current] + weight
            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
                previous[neighbour] = current

    return distance, previous


def build_path(previous, destination):
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = previous[current]
    return list(reversed(path))


graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 1)],
    "C": [("B", 2), ("D", 5)],
    "D": []
}

source = "A"
distances, previous = dijkstra(graph, source)

print("Starting vertex:", source)
for vertex in graph:
    if distances[vertex] == float("inf"):
        print(vertex, "is not reachable")
    else:
        print("Shortest distance to", vertex, "=", distances[vertex])
        print("Path:", " -> ".join(build_path(previous, vertex)))
