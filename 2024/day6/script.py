# from pprint import pprint
path = "."
block = "#"
up = "^"
down = "v"
right = ">"
left = "<"
directions = {up: (-1, 0), right: (0, 1), down: (1, 0), left: (0, -1)}
direction_pointer = {up: right, right: down, down: left, left: up}


def process_input(path):

    # we want to return a list of containing strings for easy iterations
    with open(path) as file:
        content = file.readlines()
    content = [line.strip("\n") for line in content]
    guard_position = None
    guard_direction = None
    for row in range(len(content)):
        for col in range(len(content[row])):
            if content[row][col] in directions:
                guard_direction = content[row][col]
                guard_position = (row, col)
                break
    return content, guard_direction, guard_position


lab, guard_direction, guard_position = process_input("input.txt")


def simulate_guard(lab, guard_direction, guard_position):
    rows = len(lab)
    cols = len(lab[0])
    visited_positions = set()
    row, col = guard_position
    direction = guard_direction

    in_bounds = True

    while in_bounds:
        visited_positions.add((row, col))
        d_row, d_col = directions[direction]
        next_r, next_c = row + d_row, col + d_col

        if 0 <= next_r < rows and 0 <= next_c < cols and lab[next_r][next_c] != "#":
            row, col = next_r, next_c

        else:
            direction = direction_pointer[direction]
        if next_r < 0 or next_r >= rows or next_c < 0 or next_c >= cols:
            in_bounds = False
    return len(visited_positions)


print(simulate_guard(lab, guard_direction, guard_position))


# Part 2

def detect_loop(lab, guard_direction, guard_position):
    rows = len(lab)
    cols = len(lab[0])
    row, col = guard_position
    loop_found = False
    exits = False
    direction = guard_direction
    visited = {(row, col, direction): 1}
    while not loop_found and not exits:
        d_row, d_col = directions[direction]
        row, col = row + d_row, col + d_col
        if 0 <= row < rows and 0 <= col < cols and lab[row][col] != block:
            if not ((row, col, direction) in visited):
                visited[(row, col, direction)] = 1
            else:
                return True
        elif 0 <= row < rows and 0 <= col < cols and lab[row][col] == block:
            row, col = row - d_row, col - d_col
            direction = direction_pointer[direction]
        if row < 0 or row >= rows or col < 0 or col >= cols:
            exits = True

    return False


def find_possible_loops(lab, guard_direction, guard_position):
    loops = 0
    new_lab = lab[:]
    for row in range(len(lab)):
        for col in range(len(lab[row])):
            if lab[row][col] == path:
                new_lab[row] = lab[row][:col] + "#" + lab[row][col + 1:]
                # pprint(new_lab)
                loop_found = detect_loop(
                    new_lab, guard_direction, guard_position)
                if loop_found:
                    loops += 1
            new_lab = lab[:]
    return loops


print(find_possible_loops(lab, guard_direction, guard_position))
