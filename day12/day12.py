def read_file():
    values = []
    with open("input_day12.txt", "r") as input_file:
        for line in input_file:
            values.append(line.strip().split("-"))
    return values


def dict_next(values):
    next_cave = {}
    for pair in values:
        if pair[0] not in next_cave:
            next_cave[pair[0]] = []
        if pair[1] not in next_cave:
            next_cave[pair[1]] = []
        next_cave[pair[0]].append(pair[1])
        next_cave[pair[1]].append(pair[0])
    return next_cave


def dict_next_2(values):
    next_cave = {}
    for pair in values:
        if pair[0] not in next_cave:
            next_cave[pair[0]] = []
        if pair[1] not in next_cave:
            next_cave[pair[1]] = []
        next_cave[pair[0]].append(pair[1])
        next_cave[pair[1]].append(pair[0])
        if pair[0] != 'start' and pair[1] != 'start' and pair[0] != 'end' and pair[1] != 'end':
            next_cave[pair[0]].append(pair[1])
            next_cave[pair[1]].append(pair[0])

    return next_cave


def part1(next_cave, path, paths):
    next_copy = {key: [i for i in value] for key, value in next_cave.items()}
    last = path[-1]

    if last == 'end':
        paths.append(path)
        return

    if last.lower() == last:
        for c in next_copy:
            if last in next_copy[c]:
                next_copy[c].remove(last)

    for cave in next_cave[last]:
        part1(next_copy, path + [cave], paths)


def part2(next_cave, path, paths, twice):
    next_copy = {key: [i for i in value] for key, value in next_cave.items()}
    last = path[-1]

    if last == 'end':
        paths.append(path)
        return

    if last == 'start' and len(path) > 1:
        return

    if last.lower() == last and last in path[:-1]:
        twice = True
        for visited in path:
            if visited.lower() == visited:
                for c in next_copy:
                    if visited in next_copy[c]:
                        next_copy[c].remove(visited)
    elif last.lower() == last and twice:
        for c in next_copy:
            if last in next_copy[c]:
                next_copy[c].remove(last)

    for cave in next_copy[last]:
        part2(next_copy, path + [cave], paths, twice)


def main():
    values = read_file()
    next_cave = dict_next(values)
    print(next_cave)

    paths = []
    part1(next_cave, ['start'], paths)
    print(len(paths))

    paths_2 = []
    next_cave_2 = dict_next(values)
    part2(next_cave_2, ['start'], paths_2, False)
    print(len(paths_2))


if __name__ == '__main__':
    main()
