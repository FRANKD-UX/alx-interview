# Minimum Operations

This project contains an algorithm to solve the "Minimum Operations" problem:

## Problem Statement

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file:
- `Copy All`: Copies all the characters present
- `Paste`: Pastes the copied characters

Given a number `n`, calculate the fewest number of operations needed to result in exactly `n` `H` characters in the file.

## Algorithm Overview

The solution is based on prime factorization. Since we can only copy all the text and paste it, the most efficient way to reach `n` characters is to find its prime factors.

- For each prime factor `p` of `n`, we need `p` operations (1 Copy All + (p-1) Paste operations)
- The sum of all prime factors (counting repetitions) gives us the minimum number of operations

## Example

For `n = 9`:
1. Start with one `H`
2. Copy All (1 operation)
3. Paste (1 operation) → `HH` (2 characters)
4. Paste (1 operation) → `HHH` (3 characters)
5. Copy All (1 operation)
6. Paste (1 operation) → `HHHHHH` (6 characters)
7. Paste (1 operation) → `HHHHHHHHH` (9 characters)

Total: 6 operations

For `n = 12`:
The prime factorization is 2 × 2 × 3 = 12
We need (2 + 2 + 3) = 7 operations

## Usage

```python
minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Time and Space Complexity

- Time Complexity: O(√n) - as we only need to check divisors up to the square root of n
- Space Complexity: O(1) - we only use a constant amount of extra space
