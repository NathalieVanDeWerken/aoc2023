import re

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    result = 0
    for line in data:
        line = line.split(": ")[1]
        winning, numbers = line.split(" | ")
        winning = set(re.split(" +", winning))
        numbers = re.split(" +", numbers)
        x = len(list(filter(lambda y:y in winning and y != '', numbers)))
        if x != 0:
            result += 2 ** (x - 1)
    return result


def part_two(data):
    cards = [1 for _ in range(len(data))]
    for line in data:
        line = line.split(": ")
        number = int(re.split(" +", line[0])[1])
        winning, numbers = line[1].split(" | ")
        winning = set(re.split(" | ", winning))
        numbers = re.split("  | ", numbers)
        x = len(list(filter(lambda y: y in winning and y != '', numbers)))
        for i in range(x):
            if number + i >= len(cards):
                continue
            cards[number + i] += cards[number - 1]
    return sum(cards)


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
