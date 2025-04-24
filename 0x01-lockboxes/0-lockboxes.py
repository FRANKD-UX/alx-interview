#!/usr/bin/python3
"""
Module for the lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    
    Args:
        boxes (list of lists): Each box contains keys to other boxes
        
    Returns:
        bool: True if all boxes can be opened, else False
    """
    if not boxes or not isinstance(boxes, list):
        return False
    
    n = len(boxes)
    if n == 0:
        return True
    
    # Keep track of which boxes we can open
    unlocked = [False] * n
    unlocked[0] = True  # First box is always unlocked
    
    # Keys we currently have
    keys = set(boxes[0])
    
    # Continue until we can't open any more boxes
    while keys:
        # Get a key from our collection
        key = keys.pop()
        
        # If the key opens a box we haven't unlocked yet and is in valid range
        if key < n and not unlocked[key]:
            unlocked[key] = True
            # Add all keys from the newly opened box
            for new_key in boxes[key]:
                if new_key < n and not unlocked[new_key]:
                    keys.add(new_key)
    
    # Check if all boxes are unlocked
    return all(unlocked)
