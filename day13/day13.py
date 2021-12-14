def read_file():
    values = set()
    folds = []
    with open("input_day13.txt", "r") as input_file:
        coord = True
        for line in input_file:
            if coord and line == "\n":
                coord = False
            elif coord:
                values.add(tuple(int(i) for i in line.strip().split(",")))
            else:
                folds.append(line.strip())
    for i in range(len(folds)):
        [p1, p2] = folds[i].split("=")
        folds[i] = [p1[-1], int(p2)]
    return values, folds


def make_grid(values):
    max_x = 0
    max_y = 0
    for coord in values:
        max_x = max(max_x, coord[0] + 1)
        max_y = max(max_y, coord[1] + 1)
    grid = [[" " for _ in range(max_x)] for _ in range(max_y)]
    for coord in values:
        grid[coord[1]][coord[0]] = "#"
    return grid


def do_fold_x(values, x_fold):
    new_values = set()
    for coord in values:
        (x, y) = coord
        if coord[0] > x_fold:
            x = 2 * x_fold - coord[0]
        new_values.add((x, y))
    return new_values


def do_fold_y(values, y_fold):
    new_values = set()
    for coord in values:
        (x, y) = coord
        if coord[1] > y_fold:
            y = 2 * y_fold - coord[1]
        new_values.add((x, y))
    return new_values


def do_fold(values, fold):
    if fold[0] == 'x':
        return do_fold_x(values, fold[1])
    else:
        return do_fold_y(values, fold[1])


def print_grid(values):
    grid = make_grid(values)
    for line in grid:
        print("".join(line))


def main():
    values, folds = read_file()
    print(values)
    print(folds)
    for f in folds:
        values = do_fold(values, f)
    print_grid(values)
    print(len(values))


if __name__ == '__main__':
    main()
