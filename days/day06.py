import re

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    result = 1
    times = [int(x) for x in re.split("\\s+", data[0].split(": ")[1].strip())]
    records = [int(x) for x in re.split("\\s+", data[1].split(": ")[1].strip())]
    for time, record in zip(times, records):
        result1 = 0
        for x in range(time + 1):
            if x * (time - x) > record: result1 += 1
        result *= result1
    return result



def part_two(data):
    result = 0
    time = int("".join(re.split("\\s+", data[0].split(": ")[1].strip())))
    record = int("".join(re.split("\\s+", data[1].split(": ")[1].strip())))
    for x in range(time + 1):
        if x * (time - x) > record: result += 1
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
