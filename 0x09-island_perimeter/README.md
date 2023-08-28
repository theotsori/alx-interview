# Island Perimeter

An island is a piece of land surrounded by water on all sides. Given a grid representation of an island where 1's represent land and 0's represent water, you are tasked with finding the perimeter of the island. The perimeter is the total length of the boundary between the land and water.

## Problem Description

Given a 2D grid `grid` representing the layout of an island, where `grid[i][j]` is 1 if the cell is land and 0 if it's water, calculate the total perimeter of the island.

**Function Signature:**
```python
def island_perimeter(grid: List[List[int]]) -> int:
    pass
```

### Example

Input:
```
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

Output:
```
16
```

Explanation: In the given grid, there are 16 total units of perimeter. Each land cell contributes 4 units to the perimeter, and there is one adjacent side shared between neighboring land cells.

### Approach

To calculate the perimeter, iterate through each land cell in the grid. For each land cell, count its surrounding water cells (0's) as part of the perimeter. Keep in mind that you should only count water cells adjacent to the current land cell.

Pseudocode:
1. Initialize a variable `perimeter` to 0.
2. Iterate through each cell in the grid:
   - If the cell is a land cell (grid[i][j] == 1):
     - Increment the `perimeter` by 4.
     - Check the neighboring cells (up, down, left, and right) and decrement `perimeter` for each adjacent land cell.
3. Return the `perimeter`.

### Implementation

Here's a possible implementation in Python:

```python
def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                    
    return perimeter
```
