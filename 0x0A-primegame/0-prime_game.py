#!/usr/bin/python3
"""
Prime Game Module

Maria and Ben play a game where they take turns choosing prime numbers
from a set of consecutive integers (1 to n) and removing that prime
and all its multiples. The player who cannot make a move loses.
"""


def sieve_of_eratosthenes(max_n):
    """
    Generate all prime numbers up to max_n using Sieve of Eratosthenes.

    Args:
        max_n: Maximum number to check for primes

    Returns:
        List of boolean values where index i is True if i is prime
    """
    if max_n < 2:
        return [False] * (max_n + 1)

    # Initialize sieve array
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Sieve algorithm
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    return is_prime


def count_primes_up_to(n, is_prime):
    """
    Count the number of prime numbers from 2 to n.

    Args:
        n: Upper limit (inclusive)
        is_prime: Boolean array from sieve

    Returns:
        Number of primes from 2 to n
    """
    if n < 2:
        return 0
    return sum(is_prime[2:n+1])


def isWinner(x, nums):
    """
    Determine the winner of the prime game across multiple rounds.

    Args:
        x: Number of rounds
        nums: Array of n values for each round

    Returns:
        Name of player who won the most rounds, or None if tie
    """
    if x <= 0 or not nums:
        return None

    # Find maximum n to optimize sieve generation
    max_n = max(nums)

    # Generate sieve for all numbers up to max_n
    is_prime = sieve_of_eratosthenes(max_n)

    # Count wins for each player
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for i in range(x):
        n = nums[i]

        # Count primes available in this round
        prime_count = count_primes_up_to(n, is_prime)

        # If odd number of primes, Maria wins (she goes first)
        # If even number of primes, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


# Test the solution with the provided example
if __name__ == "__main__":
    # Test case from the problem
    result = isWinner(3, [4, 5, 1])
    print(f"Test case [4, 5, 1]: {result}")

    # Additional test case
    result2 = isWinner(5, [2, 5, 1, 4, 3])
    print(f"Test case [2, 5, 1, 4, 3]: {result2}")

    # Let's trace through the first example step by step
    print("\nTracing first example:")
    print("Round 1 (n=4): Primes are [2, 3] -> 2 primes (even) -> Ben wins")
    print(
        "Round 2 (n=5): Primes are [2, 3, 5] -> "
        "3 primes (odd) -> Maria wins")
    print("Round 3 (n=1): No primes -> 0 primes (even) -> Ben wins")
    print("Ben wins 2 rounds, Maria wins 1 round -> Ben is overall winner")
