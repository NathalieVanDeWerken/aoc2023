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
        values = [int(x) for x in line.split(" ")]
        result += extrapolate(values) + values[-1]
    return result

def extrapolate(values):
    sums = []
    for i in range(len(values) - 1):
        sums.append(values[i + 1] - values[i])
    if all(x == 0 for x in sums):
        return 0
    else: return sums[-1] + extrapolate(sums)


def part_two(data):
    result = 0
    for line in data:
        values = [int(x) for x in line.split(" ")]
        result += values[0] - extrapolate2(values)
    return result

def extrapolate2(values):
    sums = []
    for i in range(len(values) - 1):
        sums.append(values[i + 1] - values[i])
    if all(x == 0 for x in sums):
        return 0
    else: return sums[0] - extrapolate2(sums)

if __name__ == "__main__":
    print(solve(load_input("small")))
    print(solve(load_input()))
    print(solve(load_input("small"), 2))
    print(solve(load_input(), 2))
