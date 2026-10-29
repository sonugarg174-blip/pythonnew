"""Floyd-Warshall: shortest distance between every pair of vertices."""

INF = float("inf")

# INF means there is no direct edge between those vertices.
distance = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

n = len(distance)

for middle in range(n):
    for start in range(n):
        for end in range(n):
            # Is going through 'middle' shorter?
            distance[start][end] = min(
                distance[start][end],
                distance[start][middle] + distance[middle][end]
            )

print("All-pairs shortest-distance matrix:")
for row in distance:
    print(["INF" if value == INF else value for value in row])
