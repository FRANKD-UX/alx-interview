# Prime Game

## Project Description

This project implements a solution to a competitive game theory problem involving prime numbers. Maria and Ben play a game where they take turns choosing prime numbers from a set of consecutive integers and removing that prime along with all its multiples. The player who cannot make a move loses.

## Game Rules

1. Given a set of consecutive integers from 1 to n
2. Players take turns choosing a prime number from the set
3. When a prime is chosen, that number and all its multiples are removed
4. Maria always goes first
5. Both players play optimally
6. The player who cannot make a move loses

## Algorithm Explanation

### Key Insight
The winner is determined by the total number of available prime numbers:
- **Odd number of primes**: Maria wins (she gets the last prime)
- **Even number of primes**: Ben wins

### Implementation Strategy

1. **Sieve of Eratosthenes**: Efficiently find all prime numbers up to the maximum n
2. **Prime Counting**: For each game round, count primes ≤ n
3. **Winner Determination**: Use parity of prime count to determine round winner
4. **Overall Winner**: Count total wins across all rounds

### Time Complexity
- **Sieve Generation**: O(n log log n) where n is the maximum number
- **Prime Counting**: O(1) per query after preprocessing
- **Overall**: O(n log log n + x) where x is number of rounds

### Space Complexity
- O(n) for storing the sieve array

## Files

- `0-prime_game.py`: Main implementation file containing the `isWinner` function
- `README.md`: This documentation file

## Usage

```python
#!/usr/bin/python3
isWinner = __import__('0-prime_game').isWinner

# Example usage
result = isWinner(3, [4, 5, 1])
print(f"Winner: {result}")  # Output: Winner: Ben
```

## Example Walkthrough

For `x = 3, nums = [4, 5, 1]`:

### Round 1 (n=4):
- Available numbers: {1, 2, 3, 4}
- Available primes: {2, 3} (2 primes - even)
- Maria picks 2, removes {2, 4} → remaining: {1, 3}
- Ben picks 3, removes {3} → remaining: {1}
- No primes left for Maria → **Ben wins**

### Round 2 (n=5):
- Available numbers: {1, 2, 3, 4, 5}
- Available primes: {2, 3, 5} (3 primes - odd)
- Since there are 3 primes and Maria goes first → **Maria wins**

### Round 3 (n=1):
- Available numbers: {1}
- Available primes: {} (0 primes - even)
- No primes for Maria to pick → **Ben wins**

**Result**: Ben wins 2 rounds, Maria wins 1 round → **Ben is the overall winner**

## Key Concepts Used

- **Prime Numbers**: Understanding and efficient identification
- **Sieve of Eratosthenes**: Optimal prime finding algorithm
- **Game Theory**: Optimal play strategy analysis
- **Dynamic Programming**: Efficient computation through preprocessing

## Requirements Met

- Python 3.4.3 compatible
- PEP 8 compliant code style
- No external package imports
- Efficient algorithm for constraints (n, x ≤ 10000)
- Proper file headers and documentation
