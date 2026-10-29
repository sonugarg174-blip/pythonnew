"""Find a path through a maze using backtracking.
0 = open cell, 1 = wall. Start is top-left; finish is bottom-right.
"""

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
rows, cols = len(maze), len(maze[0])
path = []
visited = set()


def find_path(row, col):
    if not (0 <= row < rows and 0 <= col < cols):
        return False
    if maze[row][col] == 1 or (row, col) in visited:
        return False

    visited.add((row, col))
    path.append((row, col))

    if (row, col) == (rows - 1, cols - 1):
        return True

    # Try down, right, up, and left.
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if find_path(row + dr, col + dc):
            return True

    path.pop()  # This route failed, so undo the last step.
    return False


if find_path(0, 0):
    print("Path as (row, column) positions:")
    print(path)
    print("Maze with path marked by *:")
    for r in range(rows):
        line = []
        for c in range(cols):
            if (r, c) in path:
                line.append("*")
            elif maze[r][c] == 1:
                line.append("#")
            else:
                line.append(".")
        print(" ".join(line))
else:
    print("No path exists.")
