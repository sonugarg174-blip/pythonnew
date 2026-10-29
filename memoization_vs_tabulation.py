"""Memoization vs Tabulation using the staircase problem.

You can climb 1 or 2 steps at a time. How many different ways to reach n?
"""


def ways_memo(n, memo=None):
    # Top-down: start with the requested problem and remember answers.
    if memo is None:
        memo = {0: 1, 1: 1}
    if n not in memo:
        memo[n] = ways_memo(n - 1, memo) + ways_memo(n - 2, memo)
    return memo[n]


def ways_tabulation(n):
    # Bottom-up: fill answers for 0, 1, 2, ... n.
    dp = [0] * (n + 1)
    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    for step in range(2, n + 1):
        dp[step] = dp[step - 1] + dp[step - 2]
    return dp[n]


n = 5
print("Staircase steps:", n)
print("Ways using memoization:", ways_memo(n))
print("Ways using tabulation:", ways_tabulation(n))
