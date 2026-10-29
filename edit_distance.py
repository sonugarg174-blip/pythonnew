"""Edit Distance (Levenshtein distance) using dynamic programming.

Allowed operations: insert a character, delete a character, replace a character.
"""


def edit_distance(first, second):
    rows, cols = len(first), len(second)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Turning a word into an empty string requires deletions.
    for i in range(rows + 1):
        dp[i][0] = i
    # Turning an empty string into a word requires insertions.
    for j in range(cols + 1):
        dp[0][j] = j

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert_cost = dp[i][j - 1]
                delete_cost = dp[i - 1][j]
                replace_cost = dp[i - 1][j - 1]
                dp[i][j] = 1 + min(insert_cost, delete_cost, replace_cost)

    return dp[rows][cols], dp


word1 = "kitten"
word2 = "sitting"
distance, table = edit_distance(word1, word2)
print("First word:", word1)
print("Second word:", word2)
print("Minimum edit distance:", distance)
print("DP table (rows = first word prefixes, columns = second word prefixes):")
for row in table:
    print(row)
