#!/usr/bin/python3
"""
This module contains the minOperations function that calculates the fewest
number of operations needed to result in exactly n H characters in a file.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H
    characters in a file.

    Args:
        n (int): The target number of H characters

    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible
    """
    # If n is 1, we already have 'H', so 0 operations needed
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Keep dividing n by its smallest prime factors
    # and summing up these factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
