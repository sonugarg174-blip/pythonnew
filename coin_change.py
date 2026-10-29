"""Coin Change: minimum number of coins to make a target amount."""


def min_coins(coins, amount):
    # dp[value] stores the fewest coins needed to make 'value'.
    dp = [float("inf")] * (amount + 1)
    chosen_coin = [None] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value and dp[value - coin] + 1 < dp[value]:
                dp[value] = dp[value - coin] + 1
                chosen_coin[value] = coin

    if dp[amount] == float("inf"):
        return -1, []

    used = []
    value = amount
    while value > 0:
        coin = chosen_coin[value]
        used.append(coin)
        value -= coin
    return dp[amount], used


coins = [1, 3, 4]
amount = 6
count, used_coins = min_coins(coins, amount)
print("Available coins:", coins)
print("Target amount:", amount)
if count == -1:
    print("The amount cannot be made with these coins.")
else:
    print("Minimum number of coins:", count)
    print("Coins used:", used_coins)
