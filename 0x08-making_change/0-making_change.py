#!/usr/bin/python3
"""
Solution for the coin change problem to find fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount

    Args:
        coins (List[int]): Values of coins available
        total (int): Target total amount

    Returns:
        int: Fewest number of coins needed, or -1 if total cannot be met
    """
    # Handle trivial cases
    if total <= 0:
        return 0

    # Initialize dp array with float('inf')
    # representing an unreachable state
    dp = [float('inf')] * (total + 1)
    # 0 coins needed to make 0 total
    dp[0] = 0

    # For each possible total from 1 to target total
    for i in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin is less than or equal to current total
            if coin <= i:
                # Update minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result, or -1 if total cannot be met
    return dp[total] if dp[total] != float('inf') else -1
