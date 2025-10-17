import math

cipher = "taskphaWL_PL4sOingpYefdngaP{_diddL40ap}y5rn_s1m37"

# Function to fill the grid row-wise
def fill_grid_rowwise(cipher, rows, cols):
    grid = [['']*cols for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(cipher):
                grid[r][c] = cipher[idx]
                idx += 1
    return grid

# Function to read grid in spiral clockwise order
def read_spiral(grid):
    rows = len(grid)
    cols = len(grid[0])
    top, bottom, left, right = 0, rows-1, 0, cols-1
    out = []

    while left <= right and top <= bottom:
        # top row
        for c in range(left, right+1):
            out.append(grid[top][c])
        top += 1
        # right column
        for r in range(top, bottom+1):
            out.append(grid[r][right])
        right -= 1
        # bottom row
        for c in range(right, left-1, -1):
            out.append(grid[bottom][c])
        bottom -= 1
        # left column
        for r in range(bottom, top-1, -1):
            out.append(grid[r][left])
        left += 1

    return ''.join(out)

# Choose grid size (7x7 worked for this cipher)
rows = 7
cols = 7

grid = fill_grid_rowwise(cipher, rows, cols)
decrypted = read_spiral(grid)

# Extract the flag inside curly braces
import re
match = re.search(r"taskphase\{.*?\}", decrypted)
if match:
    flag = match.group(0)
    print("Flag found:", flag)
else:
    print("No flag found. Decrypted text:", decrypted)
