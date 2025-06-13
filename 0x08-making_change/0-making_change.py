#!/usr/bin/python3
"""
Coin change problem solution using dynamic programming
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.
    
    Args:
        coins: List of coin denominations (integers > 0)
        total: Target amount to make
    
    Returns:
        Minimum number of coins needed, or -1 if impossible, or 0 if total <= 0
    """
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity for all amounts except 0
    # dp[i] represents minimum coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0
    
    # For each amount from 1 to total
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin value is not greater than current amount
            if coin <= amount:
                # Update dp[amount] with minimum coins needed
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result: -1 if impossible, otherwise minimum coins needed
    return dp[total] if dp[total] != float('inf') else -1
