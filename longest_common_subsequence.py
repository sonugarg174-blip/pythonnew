"""Longest Common Subsequence (LCS) using dynamic programming.

A subsequence keeps the order of characters but need not be consecutive.
Example: ABCD and ACBD have an LCS such as ABD or ACD, of length 3.
"""


def lcs(first, second):
    rows, cols = len(first), len(second)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct one LCS by walking backwards through the table.
    i, j = rows, cols
    answer = []
    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            answer.append(first[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    answer.reverse()
    return dp[rows][cols], "".join(answer)


a = "ABCBDAB"
b = "BDCABA"
length, sequence = lcs(a, b)
print("First string:", a)
print("Second string:", b)
print("LCS length:", length)
print("One LCS:", sequence)
