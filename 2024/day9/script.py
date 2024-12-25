path = "test.txt"


def process_input(path):
    with open(path) as file:
        content = file.read().strip("\n")
    disk_map = []
    block_id = 0
    for i in range(len(content)):
        is_file = i % 2 == 0
        x = int(content[i])
        if is_file:
            disk_map += [block_id] * x
            block_id += 1
        else:
            disk_map += [-1] * x

    return disk_map


disk_map = process_input(path)


# Part 1

def check_sum(disk_map):
    new_disk = disk_map[:]
    i, j = 0, len(disk_map) - 1
    while i < j:
        if disk_map[i] != -1:
            i += 1
        if disk_map[j] == -1:
            j -= 1
        if disk_map[i] == -1 and disk_map[j] != -1 and i < len(disk_map) - 1 and j >= 0:
            new_disk[i], new_disk[j] = new_disk[j], new_disk[i]
            i += 1
            j -= 1
    total = 0
    for i, item in enumerate(new_disk):
        if item != -1:
            total += i * item
        else:
            break
    return total


print(disk_map)
print(check_sum(disk_map))


# Part 2

def check_sum_2(disk_map):
    new_disk = []
    ln = len(disk_map)
    i = 0
    while i < ln:
        j = i
        while j < ln and disk_map[i] == disk_map[j]:
            j += 1

        new_disk.append((i, j))
        i = j
    print(new_disk)


check_sum_2(disk_map)
