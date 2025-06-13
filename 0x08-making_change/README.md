# 0x08. Making Change

## Description
This project implements a solution to the classic coin change problem using dynamic programming. The goal is to find the minimum number of coins required to make up a given total amount from a list of coin denominations.

## Problem Statement
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

## Algorithm Approach
The solution uses **Dynamic Programming** instead of a greedy approach because:
- Greedy algorithms don't always work for arbitrary coin systems
- Dynamic programming guarantees the optimal solution
- It handles edge cases where greedy fails (e.g., coins [1, 3, 4] for total 6)

## Time and Space Complexity
- **Time Complexity**: O(total × number of coins)
- **Space Complexity**: O(total)

## Key Features
- Handles edge cases (total ≤ 0, impossible combinations)
- Optimal substructure: builds solution from smaller subproblems
- Bottom-up approach for efficiency

## Function Prototype
```python
def makeChange(coins, total)
```

### Parameters
- `coins`: List of coin denominations (positive integers)
- `total`: Target amount to achieve

### Return Values
- `0`: If total is 0 or less
- `-1`: If total cannot be achieved with given coins
- `positive integer`: Minimum number of coins needed

## Usage Example
```python
makeChange([1, 2, 25], 37)  # Returns 7 (25 + 10*1 + 1*2)
makeChange([1256, 54, 48, 16, 102], 1453)  # Returns -1 (impossible)
```

## Files
- `0-making_change.py`: Main implementation
- `0-main.py`: Test file
- `README.md`: Project documentation

## Requirements
- Python 3.4.3+
- Ubuntu 20.04 LTS
- PEP 8 style compliance
- Executable files with proper shebang
