def read_file():
    transitions = {}
    first = True
    with open("input_day14.txt", "r") as input_file:
        for line in input_file:
            if not first:
                read_line = line.strip()
                transitions[read_line[0:2]] = read_line[-1]
            elif line == "\n":
                first = False
            else:
                start = line.strip()
    return start, transitions


def step(polymer, transitions):  # for part 1
    place = 0
    while place < len(polymer) - 1:
        pair = polymer[place] + polymer[place + 1]
        if pair in transitions:
            place += 1
            polymer.insert(place, transitions[pair])
        place += 1
    return polymer


def pair_counts(polymer):  # turns list/string into dict count of pairs for part 2
    pairs = {}
    for place in range(len(polymer) - 1):
        pair = polymer[place] + polymer[place + 1]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    return pairs


def step_counts(polymer_counts, transitions, counts):  # for part 2
    new_polymer = {}
    for pair in polymer_counts:
        if pair in transitions:
            inserted = transitions[pair]
            new_1 = pair[0] + inserted
            new_2 = inserted + pair[1]
            if new_1 in new_polymer:
                new_polymer[new_1] += polymer_counts[pair]
            else:
                new_polymer[new_1] = polymer_counts[pair]
            if new_2 in new_polymer:
                new_polymer[new_2] += polymer_counts[pair]
            else:
                new_polymer[new_2] = polymer_counts[pair]
            if inserted in counts:
                counts[inserted] += polymer_counts[pair]
            else:
                counts[inserted] = polymer_counts[pair]
    return new_polymer


def quantities(polymer):  # for part 1 - counts frequency in list/string
    counts = {}
    for each in polymer:
        if each in counts:
            counts[each] += 1
        else:
            counts[each] = 1
    return counts


def big_sub_small(counts):  # finds most frequent and last frequent and subtracts
    letters = [l for l in counts.keys()]
    biggest = 0
    smallest = counts[letters[0]]
    for letter in letters:
        biggest = max(biggest, counts[letter])
        smallest = min(smallest, counts[letter])
    return biggest - smallest


def part1(start, transitions):
    polymer = [c for c in start]
    for i in range(10):
        step(polymer, transitions)
    print("".join(polymer))
    counts = quantities(polymer)
    print(big_sub_small(counts))


def part2(start, transitions):
    polymer = pair_counts([c for c in start])
    counts = quantities(start)
    for i in range(40):
        polymer = step_counts(polymer, transitions, counts)
    print(big_sub_small(counts))


def main():
    start, transitions = read_file()
    part1(start, transitions)
    part2(start, transitions)


if __name__ == '__main__':
    main()
