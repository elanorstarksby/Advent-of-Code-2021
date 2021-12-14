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


def step(polymer, transitions):
    place = 0
    while place < len(polymer) - 1:
        pair = polymer[place] + polymer[place + 1]
        if pair in transitions:
            place += 1
            polymer.insert(place, transitions[pair])
        place += 1
    return polymer


def pair_counts(polymer):
    pairs = {}
    for place in range(len(polymer) - 1):
        pair = polymer[place] + polymer[place + 1]
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    return pairs


def step_counts(polymer_counts, transitions, counts):
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
        # else:
        #     if pair in new_polymer:
        #         new_polymer[pair] += polymer_counts[pair]
        #     else:
        #         new_polymer[pair] = polymer_counts[pair]
    return new_polymer


def quantities(polymer):
    counts = {}
    for each in polymer:
        if each in counts:
            counts[each] += 1
        else:
            counts[each] = 1
    return counts


# def quantities_from_pairs(polymer_pairs):
#     counts = {}
#     for pair, count in polymer_pairs.items():
#         p0 = pair[0]
#         p1 = pair[1]
#         if p0 in counts:
#             counts[p0] += count
#         else:
#             counts[p0] = count
#         if p1 in counts:
#             counts[p1] += count
#         else:
#             counts[p1] = count
#     for c in counts:
#         counts[c] /= 2
#     return counts


def big_sub_small(counts):
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
    # first, last = polymer[0], polymer[-1]
    counts = quantities(start)
    print("!", counts)
    for i in range(40):
        polymer = step_counts(polymer, transitions, counts)
    print(big_sub_small(counts))

    # print(big_sub_small(polymer))


def main():
    start, transitions = read_file()
    part1(start, transitions)
    part2(start, transitions)


if __name__ == '__main__':
    main()
