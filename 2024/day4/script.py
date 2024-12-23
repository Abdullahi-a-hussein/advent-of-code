
# --- Day 4: Ceres Search ---

def process_input(path):
    with open(path) as file:
        content = file.readlines()
    content = [entry.strip("\n") for entry in content]
    return content


def part_1(content, counter, center):
    total = 0
    for row in range(len(content)):
        for col in range(len(content[0])):
            if content[row][col] == center:
                total += counter(content, row, col)
    return total


def count_neighbors(content, row, col):
    col_ln = len(content[row])
    count = 0
    target = "MAS"  # target word for the search
    tl = len(target)  # target length
    # check horizontal
    left = col - 1
    right = col + 1
    i = 0
    while i < 3 and left >= 0 and content[row][left] == target[i]:
        i += 1
        left -= 1
    if i == 3:
        count += 1

    i = 0
    while i < 3 and right < col_ln and content[row][right] == target[i]:
        i += 1
        right += 1
    if i == 3:
        count += 1

    # Check vertical

    up = row - 1
    down = row + 1
    i = 0
    while i < 3 and up >= 0 and content[up][col] == target[i]:
        up -= 1
        i += 1
    if i == 3:
        count += 1

    i = 0
    while i < 3 and down < len(content) and content[down][col] == target[i]:
        down += 1
        i += 1
    if i == 3:
        count += 1

    # check diagnols

    # checking left to right
    up = row - 1
    left = col - 1
    i = 0
    while i < 3 and (up >= 0 and left >= 0) and content[up][left] == target[i]:
        i += 1
        up -= 1
        left -= 1
    if i == 3:
        count += 1

    down = row + 1
    right = col + 1
    i = 0
    while i < 3 and (down < len(content) and right < len(content[row])) and content[down][right] == target[i]:
        i += 1
        down += 1
        right += 1
    if i == 3:
        count += 1

    # Checking the other diagnol
    up = row - 1
    right = col + 1
    i = 0
    while i < 3 and (up >= 0 and right < len(content[row])) and content[up][right] == target[i]:
        i += 1
        up -= 1
        right += 1
    if i == 3:
        count += 1

    down = row + 1
    left = col - 1
    i = 0
    while i < 3 and (down < len(content) and left >= 0) and content[down][left] == target[i]:
        i += 1
        down += 1
        left -= 1
    if i == 3:
        count += 1
    return count


def count_neighbors_2(content, row, col):
    pass


p = ["MMMSXXMASM",
     "MSAMXMSMSA",
     "AMXSXMAAMM",
     "MSAMASMSMX",
     "XMASAMXAMM",
     "XXAMMXXAMA",
     "SMSMSASXSS",
     "SAXAMASAAA",
     "MAMMMXMMMM",
     "MXMXAXMASX",]

problem_input = process_input("input.txt")
print(part_1(problem_input, count_neighbors, "X"))
