def read_file():
    values = []
    with open("input_day11.txt", "r") as input_file:
        for line in input_file:
            values.append([int(i) for i in line.strip()])
    return values


def flash_effects(values, row, col):
    if row > 0:
        if values[row - 1][col] != 0:
            values[row - 1][col] += 1  # up
        if col > 0 and values[row - 1][col - 1] != 0:
            values[row - 1][col - 1] += 1  # up and left
        if col < len(values[0]) - 1 and values[row - 1][col + 1] != 0:
            values[row - 1][col + 1] += 1  # up and right
    if col > 0 and values[row][col - 1] != 0:
        values[row][col - 1] += 1  # left

    if row < len(values) - 1:
        if values[row+1][col] != 0:
            values[row + 1][col] += 1  # down
        if col > 0 and values[row + 1][col - 1] != 0:
            values[row + 1][col - 1] += 1  # down and left
        if col < len(values[0]) - 1 and values[row + 1][col + 1] != 0:
            values[row + 1][col + 1] += 1  # down and right
    if col < len(values) - 1 and values[row][col + 1] != 0:
        values[row][col + 1] += 1  # right

    return values


def progress_step(values):
    for row in range(len(values)):
        for col in range(len(values[row])):
            values[row][col] += 1

    flashes = 0
    while any(any(x >= 10 for x in row) for row in values):
        for row in range(len(values)):
            for col in range(len(values[row])):
                if values[row][col] >= 10:
                    values = flash_effects(values, row, col)
                    values[row][col] = 0
                    flashes += 1
    all_flash = flashes == len(values) * len(values[0])
    return values, flashes, all_flash


def part1(values):
    flashes = 0
    for step in range(1, 101):
        values, f, _ = progress_step(values)
        flashes += f
    return flashes


def part2(values):
    all_flash = False
    step = 0
    while not all_flash:
        step += 1
        values, _, all_flash = progress_step(values)
    return step


def main():
    values = read_file()
    print(part1(values))
    values = read_file()
    print(part2(values))


if __name__ == '__main__':
    main()
