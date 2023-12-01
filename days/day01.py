from curses.ascii import isdigit

from lib import load_input


def solve(data, part=1):
    lines = data.splitlines()
    if part == 1:
        return part_one(lines)
    elif part == 2:
        return part_two(lines)


def part_one(data):
    result = 0
    for x in data:
        y = list(filter(lambda z: isdigit(z), x))
        result += int(y[0] + y[-1])
    return result


def part_two(data):
    result = 0
    for x in data:
        x = (x.replace('one', "on1e").replace('two', "tw2o").replace("three", "thre3e").replace("four", "fou4r")
             .replace("five", "fiv5e").replace("six", "si6x").replace("seven", "seve7n").replace("eight", "eigh8t")
             .replace("nine", "nin9e"))
        y = list(filter(lambda z: isdigit(z), x))
        result += int(y[0] + y[-1])
    return result


if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small2"), 2))
    print(solve(load_input(), 2))
