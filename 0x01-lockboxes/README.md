# Lockboxes

## Description
This project contains a solution to the lockboxes problem, where we need to determine if all boxes can be opened given a set of keys.

## Task
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened:
* Prototype: `def canUnlockAll(boxes)`
* `boxes` is a list of lists
* A key with the same number as a box opens that box
* You can assume all keys will be positive integers
* There can be keys that do not have boxes
* The first box `boxes[0]` is unlocked
* Return `True` if all boxes can be opened, else return `False`

## Files
* `0-lockboxes.py`: Contains the function to determine if all boxes can be opened.

## Usage
```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```
