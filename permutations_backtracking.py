"""Generate all permutations of a list using backtracking."""

items = [1, 2, 3]
results = []


def generate(position):
    if position == len(items):
        results.append(items.copy())
        return

    for index in range(position, len(items)):
        # Put one candidate in the current position.
        items[position], items[index] = items[index], items[position]
        generate(position + 1)
        # Restore the list before trying the next candidate.
        items[position], items[index] = items[index], items[position]


generate(0)
print("All permutations:")
for result in results:
    print(result)
print("Total permutations:", len(results))
