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
        game = line.split(": ")
        ind = int(game[0].split(" ")[-1])
        rounds = re.split("; |, ", game[1])
        if mapping(rounds): result += ind

    return result


def mapping(list):
    for x in list:
        x = x.split(" ")
        if x[1] == "blue" and int(x[0]) > 14:
            return False
        if x[1] == "green" and int(x[0]) > 13:
            return False
        if x[1] == "red" and int(x[0]) > 12:
            return False
    return True


def part_two(data):
    result = 0
    for line in data:
        game = line.split(": ")
        rounds = re.split("; |, ", game[1])
        result += power(rounds)
    return result


def power(game):
    min_red, min_blue, min_green = 0, 0, 0
    for x in game:
        x = x.split(" ")
        if x[1] == "blue":
            min_blue = max(min_blue, int(x[0]))
        if x[1] == "green":
            min_green = max(min_green, int(x[0]))
        if x[1] == "red":
            min_red = max(min_red, int(x[0]))
    return min_red * min_green * min_blue


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
