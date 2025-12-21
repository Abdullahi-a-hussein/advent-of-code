
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


def part2(starting: int, rotations: list[int]) -> int:
    count = 0
    current = starting
    for entry in rotations:
        rotation = int(entry[1:])
        if entry[0] == "R":
            current += rotation
            if current > 100:
                count += current // 100
                current = current % 100
        else:
            current -= rotation
            if current < 0:
                if not (-current == rotation and rotation < 100):
                    count += (100 - current) // 100
                current = current % 100
        if current == 0 or current == 100:
            count += 1
            current %= 100
    return count


if __name__ == "__main__":
    starting = 50
    path1 = "2025/day1/example.txt"
    path2 = "2025/day1/in.txt"
    rotations = process_input(path2)
    count = part2(starting, rotations)
    print(count)
