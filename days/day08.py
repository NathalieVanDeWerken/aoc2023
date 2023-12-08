import string
import numpy as np

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    instructions = list(data[0])
    map = {}
    for line in data[2:]:
        loc, to = line.split(" = ")
        L, R = to[1: -1].split(", ")
        map[loc] = (L, R)
    dest = "AAA"
    moves = 0
    while dest != "ZZZ":
        ins = instructions[moves % len(instructions)]
        if ins == "L":
            dest = map[dest][0]
        else:
            dest = map[dest][1]
        moves += 1
    return moves


def part_two(data):
    instructions = list(data[0])
    map1 = {}
    dest = []
    for line in data[2:]:
        loc, to = line.split(" = ")
        L, R = to[1: -1].split(", ")
        map1[loc] = (L, R)
        if loc.endswith("A"):
            dest.append(loc)
    destinations = []
    for x in dest:
        y = x
        moves = 0
        while not y.endswith("Z"):
            ins = instructions[moves % len(instructions)]
            if ins == "L":
                y = map1[y][0]
            else:
                y = map1[y][1]
            moves += 1
        destinations.append(moves)
    return np.lcm.reduce(destinations)


if __name__ == "__main__":
    print(solve(load_input("small2")))
    print(solve(load_input()))
    print(solve(load_input("small3"), 2))
    print(solve(load_input(), 2))
