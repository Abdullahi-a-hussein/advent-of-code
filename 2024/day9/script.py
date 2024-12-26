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
    marker = []
    new_disk = disk_map[:]
    ln = len(disk_map)
    i = 0
    curr = disk_map[0]
    while i < ln:
        j = i
        while j < ln and disk_map[i] == disk_map[j]:
            curr = disk_map[j]
            j += 1

        marker.append([curr, [i, j - i]])
        i = j
    end = ln(marker) - 1
    while end > 0:
        start = 0
        while start < end:

            # 1. end is  is not -1
            # start is -1 and start ln is greater than end ln
            # > go to  disk and swap element start[1][1] += 1 until end[1][1]
            # > update marker at the given positions
            # 1. if start end[1][1] == srart[1][1]
            # swap marker[start], marker[end] = marker[end], marker[start]
            # 2. if start is greater than end
            # define new entry for [start[0], [end[1[0] + end[1][1]]
            # start[0], start[1][0], start[1][1] = end[0], end[1][0], end[1][1]
            pass


check_sum_2(disk_map)
