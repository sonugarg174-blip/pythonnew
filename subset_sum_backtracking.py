"""Print subsets whose sum equals the target value."""

numbers = [2, 3, 5, 6, 8]
target = 10
solutions = []


def search(index, chosen, total):
    if total == target:
        solutions.append(chosen.copy())
        return
    if index == len(numbers) or total > target:
        return

    # Choice 1: include the current number.
    chosen.append(numbers[index])
    search(index + 1, chosen, total + numbers[index])
    chosen.pop()  # Backtrack.

    # Choice 2: skip the current number.
    search(index + 1, chosen, total)


search(0, [], 0)
print("Numbers:", numbers)
print("Target:", target)
print("Subsets that add up to target:")
for subset in solutions:
    print(subset)
