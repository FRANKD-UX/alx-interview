# 0x09. Island Perimeter

## Description

This project implements a solution to calculate the perimeter of an island in a 2D grid. The grid is represented as a list of lists where `0` represents water and `1` represents land. The goal is to determine the total perimeter of the island by counting the exposed edges of land cells.

## Learning Objectives

By completing this project, you will understand:

- How to work with 2D arrays (matrices) in Python
- How to navigate through adjacent cells in a grid
- How to apply conditional logic to solve geometric problems
- How to use nested loops for grid traversal
- How to count and accumulate values based on specific conditions

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All files must be executable

## Problem Description

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in grid:

- `grid` is a list of list of integers:
  - `0` represents water
  - `1` represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

## Algorithm Approach

The solution works by:

1. Iterating through each cell in the grid
2. For each land cell (value = 1), checking its 4 adjacent cells (up, down, left, right)
3. Counting how many sides are exposed to water or grid boundaries
4. Summing up all the exposed sides to get the total perimeter

### Time Complexity: O(m × n) where m is rows and n is columns
### Space Complexity: O(1) - constant extra space

## Files

- `0-island_perimeter.py`: Contains the main `island_perimeter()` function
- `0-main.py`: Test file to verify the solution works correctly
- `README.md`: This file

## Usage

```bash
# Make files executable
chmod +x 0-island_perimeter.py
chmod +x 0-main.py

# Run the test
./0-main.py
```

## Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
```

## Testing

The project includes a test case that should output `12` for the given grid. You can add additional test cases to verify the solution works with different scenarios:

- Single cell islands
- Empty grids (no islands)
- Different island shapes

## Author

This project is part of the ALX Interview Preparation curriculum.

## Repository

- **GitHub repository**: `alx-interview`
- **Directory**: `0x09-island_perimeter`
- **Files**: `0-island_perimeter.py`, `0-main.py`, `README.md`# 0x09. Island Perimeter

## Description

This project implements a solution to calculate the perimeter of an island in a 2D grid. The grid is represented as a list of lists where `0` represents water and `1` represents land. The goal is to determine the total perimeter of the island by counting the exposed edges of land cells.

## Learning Objectives

By completing this project, you will understand:

- How to work with 2D arrays (matrices) in Python
- How to navigate through adjacent cells in a grid
- How to apply conditional logic to solve geometric problems
- How to use nested loops for grid traversal
- How to count and accumulate values based on specific conditions

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All files must be executable

## Problem Description

Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in grid:

- `grid` is a list of list of integers:
  - `0` represents water
  - `1` represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

## Algorithm Approach

The solution works by:

1. Iterating through each cell in the grid
2. For each land cell (value = 1), checking its 4 adjacent cells (up, down, left, right)
3. Counting how many sides are exposed to water or grid boundaries
4. Summing up all the exposed sides to get the total perimeter

### Time Complexity: O(m × n) where m is rows and n is columns
### Space Complexity: O(1) - constant extra space

## Files

- `0-island_perimeter.py`: Contains the main `island_perimeter()` function
- `0-main.py`: Test file to verify the solution works correctly
- `README.md`: This file

## Usage

```bash
# Make files executable
chmod +x 0-island_perimeter.py
chmod +x 0-main.py

# Run the test
./0-main.py
```

## Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))  # Output: 12
```

## Testing

The project includes a test case that should output `12` for the given grid. You can add additional test cases to verify the solution works with different scenarios:

- Single cell islands
- Empty grids (no islands)
- Different island shapes

## Author

This project is part of the ALX Interview Preparation curriculum.

## Repository

- **GitHub repository**: `alx-interview`
- **Directory**: `0x09-island_perimeter`
