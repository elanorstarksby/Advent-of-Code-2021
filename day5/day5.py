def read_file():
    lines = []
    with open("input_day5.txt", "r") as input_file:
        line_num = 0
        for line in input_file:
            (start, _, end) = line.strip().split(" ")
            (x1, y1) = (int(i) for i in start.split(","))
            (x2, y2) = (int(i) for i in end.split(","))
            lines.append({"start_x": x1, "start_y": y1, "end_x": x2, "end_y": y2})
            line_num += 1
    return lines


def add_point(grid, point):
    if point[1] >= len(grid):
        for i in range(len(grid) - 1, point[1]):
            grid.append([0 for _ in range(len(grid[0]))])
    if point[0] >= len(grid[0]):
        for row_num in range(len(grid)):
            grid[row_num] += [0 for _ in range(len(grid[row_num]) - 1, point[0])]
    grid[point[1]][point[0]] += 1
    return grid


def diag_points(line):
    points = []
    xs = range(line["start_x"], line["end_x"]+1)
    if not xs:
        xs = range(line["start_x"], line["end_x"]-1, -1)

    ys = range(line["start_y"], line["end_y"]+1)
    if not ys:
        ys = range(line["start_y"], line["end_y"]-1, -1)
    for i in range(len(xs)):
        points.append([xs[i], ys[i]])
    return points


def draw_grid(lines):
    grid = [[0]]
    for line in lines:
        if line["start_x"] == line["end_x"]:
            min_x = min(line["start_x"], line["end_x"])
            max_x = max(line["start_x"], line["end_x"])
            min_y = min(line["start_y"], line["end_y"])
            max_y = max(line["start_y"], line["end_y"])
            for i in range(min_y, max_y + 1):
                grid = add_point(grid, [min_x, i])
        elif line["start_y"] == line["end_y"]:
            min_x = min(line["start_x"], line["end_x"])
            max_x = max(line["start_x"], line["end_x"])
            min_y = min(line["start_y"], line["end_y"])
            max_y = max(line["start_y"], line["end_y"])
            for i in range(min_x, max_x + 1):
                grid = add_point(grid, [i, min_y])
        # part 2 only:
        else:
            points = diag_points(line)
            for point in points:
                grid = add_point(grid, point)
    return grid


def count_points(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] > 1:
                count += 1
    return count


if __name__ == '__main__':
    lines = read_file()

    grid = draw_grid(lines)

    print(count_points(grid))
