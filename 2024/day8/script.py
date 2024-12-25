# --- Day 8: Resonant Collinearity ---

# Antenas with the same frequency
# one twice as far as as the other
# any pair of antenas with the same frequency, there are two
# antinodes; one on each side.
# Antinodes can occur locations that contain antenas


def process_input(path):
    with open(path) as file:
        content = file.readlines()
    content = [row.strip("\n") for row in content]
    rows = len(content)
    cols = len(content[0])

    marker = {}
    for i, row in enumerate(content):
        for j, char in enumerate(row):
            if char.isalnum() and not char in marker:
                marker[char] = [(i, j)]
            elif char.isalnum() and char in marker:
                marker[char].append((i, j))
    return marker, rows, cols


antenas, rows, cols = process_input("input.txt")

# Part 1


def dist(p1, p2): return (p2[0]-p1[0], p2[1]-p1[1])
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def subtract(x, y): return (x[0] - y[0], x[1] - y[1])


def find_antinodes(antenas, rows, cols):
    antinodes = set()
    for loc in antenas.values():
        for i in range(len(loc)):
            for j in range(i + 1, len(loc)):
                p1, p2 = loc[i], loc[j]
                d = dist(p1, p2)
                ant1 = add(p2, d)
                ant2 = subtract(p1, d)
                if 0 <= ant1[0] < rows and 0 <= ant1[1] < cols:
                    antinodes.add(ant1)
                if 0 <= ant2[0] < rows and 0 <= ant2[1] < cols:
                    antinodes.add(ant2)
    return len(antinodes)


# print(find_antinodes(antenas, rows, cols))


# Part 2

def find_antinodes_2(antenas, rows, cols):
    antinodes = set()
    for antena in antenas.values():
        for i in range(len(antena)):
            for j in range(len(antena)):
                if i == j:
                    continue
                p, q = antena[i], antena[j]
                d = dist(p, q)
                while 0 <= p[0] < rows and 0 <= p[1] < cols:
                    antinodes.add(p)
                    p = subtract(p, d)

    return len(antinodes)


print(find_antinodes_2(antenas, rows, cols))
