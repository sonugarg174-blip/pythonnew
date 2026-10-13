graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
    'D': ['E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': []
}

visited = set()
count = 0

for node in graph:
    if node not in visited:
        count += 1
        stack = [node]

        while stack:
            current = stack.pop()

            if current not in visited:
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

print("Number of trees:", count)
