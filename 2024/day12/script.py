# --- Day 12: Garden Groups ---

from pprint import pprint

path = "day12/input.txt"


def process_input(path):
    with open(path) as file:
        content = [row.strip("\n").strip(" ") for row in file.readlines()]
    return content


garden = process_input(path)

rows = len(garden)
cols = len(garden[0])

# Part 1


def extract_region(grid, row, col, plot):
    stack = [(row, col)]
    seen = {(row, col)}
    while len(stack) > 0:
        cr, cc = stack.pop()
        for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc+1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if (nr, nc) not in seen:
                if grid[nr][nc] == plot:
                    cr, cc = nr, nc
                    seen.add((cr, cc))
                    stack.append((cr, cc))
    return plot, seen


def regions(grid):
    seen = set()
    found = []
    for row, region in enumerate(grid):
        for col, plot in enumerate(region):
            if (row, col) not in seen:
                regs = extract_region(grid, row, col, plot)
                found.append(regs)
                seen = seen.union(regs[1])
    return found


regs = regions(garden)


def cost(grid, regions):
    total = 0
    for val, region in regions:
        prem, area = 0, len(region)
        for row, col in region:
            for nr, nc in [(row-1, col), (row + 1, col), (row, col-1), (row, col+1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    prem += 1
                elif grid[nr][nc] != val:
                    prem += 1
        total += area * prem
    return total


print(cost(garden, regs))
