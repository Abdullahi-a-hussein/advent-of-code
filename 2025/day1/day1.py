
def process_input(path: str) -> list[str]:
    with open(path, 'r') as file:
        content = [line.strip("\n") for line in file.readlines()]
    return content


def part1(starting: int, rotations: list[str]) -> int:
    count = 0
    current = starting
    for entry in rotations:
        rotation = int(entry[1:])
        if entry[0] == "L":
            current -= rotation

        else:
            current += rotation
        while current < 0 or current > 99:
            if current < 0:
                current = 100 + current
            elif current > 99:
                current = current - 100
        if current == 0:
            count += 1
    return count


def part2(starting: int, rotations: list[str]) -> int:
    right = "R"
    left = "L"
    count = 0
    current = starting
    for entry in rotations:
        distance = int(entry[1:])
        direction = entry[0]
        revolutions = distance // 100
        if direction == right:
            current += (distance % 100)
            count += current // 100
            current %= 100
        else:
            step = distance % 100
            d_target = current
            if d_target != 0:
                if step >= d_target:
                    count += 1
                    current = (100 - (step - d_target)) % 100
                else:
                    current -= step
            else:
                current = (100 - step) % 100
        count += revolutions
    return count


if __name__ == "__main__":
    starting = 50
    path1 = "2025/day1/example.txt"
    path2 = "2025/day1/in.txt"
    rotations = process_input(path2)
    count = part2(starting, rotations)
    print(count)
