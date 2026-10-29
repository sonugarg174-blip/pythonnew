"""Longest Increasing Subsequence (LIS), simple O(n^2) DP version."""


def lis(numbers):
    if not numbers:
        return 0, []

    dp = [1] * len(numbers)
    previous = [-1] * len(numbers)

    for i in range(len(numbers)):
        for j in range(i):
            if numbers[j] < numbers[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                previous[i] = j

    end = max(range(len(numbers)), key=lambda index: dp[index])
    length = dp[end]
    sequence = []
    while end != -1:
        sequence.append(numbers[end])
        end = previous[end]
    sequence.reverse()
    return length, sequence


values = [10, 9, 2, 5, 3, 7, 101, 18]
length, sequence = lis(values)
print("Numbers:", values)
print("LIS length:", length)
print("One longest increasing subsequence:", sequence)
