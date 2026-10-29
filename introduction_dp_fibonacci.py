"""Introduction to Dynamic Programming: Fibonacci three ways."""


def fib_recursive(n):
    """Simple recursion: easy to understand but repeats work."""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_memo(n, memo=None):
    """Memoization: top-down recursion plus a cache."""
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tabulation(n):
    """Tabulation: solve smaller values first, from the bottom up."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


n = 10
print("Fibonacci number at position", n)
print("Plain recursion:", fib_recursive(n))
print("Memoization:", fib_memo(n))
print("Tabulation:", fib_tabulation(n))
