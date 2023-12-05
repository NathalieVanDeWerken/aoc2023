import re

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(data)
    elif part == 2:
        return part_two(data)


def part_one(data):
    data =data.split("\n\n")
    seeds = []
    mappings = {}
    for part in data:
        category, mapping = part.split(":")
        if category == "seeds":
            seeds = [int(x) for x in re.split("\\s+", mapping.strip())]
            for i in seeds:
                mappings[i] = i
        else:
            mappings2 = mappings.copy()
            for line in mapping.strip().splitlines():
                deststart, sourstart, rangelen = [int(x) for x in re.split("\\s+", line)]
                for ind, val in mappings.items():
                    if sourstart <= val < sourstart + rangelen:
                        mappings2[ind] = deststart + (val - sourstart)
            mappings = mappings2
    locations = list(map(lambda x: mappings[x], seeds))
    return min(locations)


def check_in_range(seeds, num):
    for i in range(0, len(seeds), 2):
        if seeds[i] <= num < seeds[i] + seeds[i + 1]:
            return True
    return False


def part_two(data):
    data = data.split("\n\n")
    seeds = [int(x) for x in re.split("\\s+", data[0].split(": ")[1].strip())]
    mappings = reversed(data[1:])
    mappings = list(map(lambda x: [[int(y) for y in re.split("\\s+", z)] for z in x.splitlines()[1:]], mappings))
    i = 0
    while True:
        to = i
        for x in mappings:
            for line in x:
                deststart, sourstart, rangelen = line
                if deststart <= to < deststart + rangelen:
                    to = sourstart + (to - deststart)
                    break
        if check_in_range(seeds, to):
            return i
        i += 1

if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
