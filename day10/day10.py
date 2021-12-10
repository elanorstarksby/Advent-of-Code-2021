def read_file():
    values = []
    with open("input_day10.txt", "r") as input_file:
        for line in input_file:
            values.append(line.strip())
    return values


def score_line(line):
    # print(line)
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    match_map = {')': '(', ']': '[', '}': '{', '>': '<'}
    line_stack = []
    for bracket in line:
        if bracket in ['(', '[', '{', '<']:
            line_stack.append(bracket)
        else:
            if len(line_stack) < 1:
                return 0
            else:
                last = line_stack.pop()
                if last != match_map[bracket]:
                    return score_map[bracket]
    return 0


class InvalidListError(Exception):
    pass


def complete(line):
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}
    match_map = {')': '(', ']': '[', '}': '{', '>': '<'}
    rev_map = {'(': ')', '{': '}', '[': ']', '<': '>'}
    line_stack = []
    for bracket in line:
        if bracket in ['(', '[', '{', '<']:
            line_stack.append(bracket)
        else:
            if len(line_stack) < 1:
                raise InvalidListError()
            else:
                line_stack.pop()
    score = 0
    for b in reversed(line_stack):
        score *= 5
        score += score_map[rev_map[b]]
    return score


def part1(values):
    score = 0
    for line in values:
        score += score_line(line)
    return score


def part2(values):
    score = 0
    incomplete = []
    for line in values:
        if score_line(line) == 0:
            incomplete.append(line)
    scores = []
    for line in incomplete:
        scores.append(complete(line))
    scores.sort()
    return scores[(len(scores)-1)/2]


def main():
    values = read_file()
    print(part1(values))
    print(part2(values))


if __name__ == '__main__':
    main()
