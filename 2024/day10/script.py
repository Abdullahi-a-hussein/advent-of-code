from collections import deque
# --- Day 10: Hoof It ---

path = "day10/input.txt"


def process_input(path):
    with open(path) as file:
        content = [[int(entry) for entry in line.strip("\n").strip(" ")]
                   for line in file.readlines()]
    return content


grid = process_input(path)

rows = len(grid)
cols = len(grid[0])

trailheads = [(r, c) for r in range(rows)
              for c in range(cols) if grid[r][c] == 0]


def bfs(grid, r, c):
    q = deque([(r, c)])
    seen = {(r, c)}
    sumit = 0
    while len(q) > 0:
        rr, cc = q.popleft()
        for nr, nc in [(rr - 1, cc), (rr + 1, cc), (rr, cc - 1), (rr, cc + 1)]:
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                continue
            if grid[nr][nc] != grid[rr][cc] + 1:
                continue
            if (nr, nc) in seen:
                continue
            seen.add((nr, nc))
            if grid[nr][nc] == 9:
                sumit += 1
            else:
                q.append((nr, nc))

    return sumit


# Part 1
print(sum(bfs(grid, r, c) for r, c in trailheads))
