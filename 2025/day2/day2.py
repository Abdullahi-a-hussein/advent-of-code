

def process_input(path: str) -> list[list[int]]:
    with open(path, 'r') as file:
        content = [entry.split("-")
                   for entry in file.read().strip("\n").split(",")]
    content = [(int(entry[0]), int(entry[1])) for entry in content]
    return content


def invalid_ids(id_range: tuple[int]) -> list[int]:
    start_id = id_range[0]
    end_range = id_range[1]
    invalid = []

    while start_id <= end_range:
        current_id = str(start_id)
        ln = len(current_id)
        if not (ln % 2):
            first_part = current_id[:ln//2]
            second_part = current_id[ln//2:]
            if first_part == second_part:
                invalid.append(start_id)
        start_id += 1

    return invalid


def part1(IDs: list[tuple[int]]) -> int:
    summed = 0
    for entry in IDs:
        summed += sum(invalid_ids(entry))
    return summed


if __name__ == "__main__":
    input1 = "2025/day2/example.txt"
    input2 = "2025/day2/in.txt"
    IDs = process_input(input2)
    result = part1(IDs)
    print(result)
