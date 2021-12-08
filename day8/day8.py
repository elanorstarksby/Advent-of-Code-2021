def read_file():
    values = []
    with open("input2.txt", "r") as input_file:
        for line in input_file:
            values.append([i for i in line.strip().split(" ")])
    return values


def get_outputs(values):
    outputs = []
    for each in values:
        divider = each.index("|")
        outputs.append(each[divider + 1:])
    return outputs


def count_uniques(outputs, uniques):
    count = 0
    for entry in outputs:
        for v in entry:
            if len(v) in uniques:
                count += 1
    return count


def output_value(output, mappings):
    st = ""
    for v in output:
        st += str(mappings["".join(sorted(v))])
    count = int(st)
    return count


def decode(patterns, uniques):
    segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    mapping = {}
    rev_map = {}
    for signal in patterns:
        l = len(signal)
        if l in uniques.keys():
            mapping["".join(sorted(signal))] = uniques[l]
            rev_map[uniques[l]] = "".join(sorted(signal))
    for signal in patterns:
        l = len(signal)
        if l == 6:
            missing = [item for item in segments if item not in signal][0]
            if missing in [c for c in rev_map[4]]:
                if missing not in [c for c in rev_map[1]]:
                    mapping["".join(sorted(signal))] = 0
                    rev_map[0] = "".join(sorted(signal))
                else:
                    mapping["".join(sorted(signal))] = 6
                    rev_map[6] = "".join(sorted(signal))
            else:
                mapping["".join(sorted(signal))] = 9
                rev_map[9] = "".join(sorted(signal))
        elif l == 5:
            missing = [item for item in segments if item not in signal]
            either_missing_in_1 = (missing[0] in [c for c in rev_map[1]]) ^ (missing[1] in [c for c in rev_map[1]])
            if not either_missing_in_1:
                mapping["".join(sorted(signal))] = 3
                rev_map[3] = "".join(sorted(signal))
            else:
                both_missing_in_4 = (missing[0] in [c for c in rev_map[4]]) and (missing[1] in [c for c in rev_map[4]])
                if both_missing_in_4:
                    mapping["".join(sorted(signal))] = 2
                    rev_map[2] = "".join(sorted(signal))
                else:
                    mapping["".join(sorted(signal))] = 5
                    rev_map[5] = "".join(sorted(signal))
    return mapping


def part_2(values, uniques):
    count = 0
    for event in values:
        event_mapping = decode(event[0:10], uniques)
        count += output_value(event[11:], event_mapping)
    return count


def main(uniques):
    values = read_file()
    output = get_outputs(values)
    print(count_uniques(output, uniques))
    print(part_2(values, uniques))


if __name__ == '__main__':
    unique = {2: 1, 4: 4, 3: 7, 7: 8}
    main(unique)
