"""Factorial with recursion and an iterative table-based approach.

Factorial: 5! = 5 * 4 * 3 * 2 * 1 = 120.
"""


def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]
    return dp[n]


n = 5
print(n, "! using recursion =", factorial_recursive(n))
print(n, "! using iterative table =", factorial_iterative(n))
print("Note: factorial is usually not a classic DP problem because subproblems do not overlap.")
