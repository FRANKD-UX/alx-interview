#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water
                                   and 1 represents land

    Returns:
        int: The perimeter of the island

    The perimeter is calculated by counting the exposed edges of land cells.
    Each land cell can contribute 0-4 units to the perimeter depending on
    how many of its sides are adjacent to water or the grid boundary.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Only process land cells
            if grid[i][j] == 1:
                # Check all 4 directions (up, down, left, right)
                # Count exposed sides

                # Check top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1

                # Check bottom
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1

                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

                # Check right
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
