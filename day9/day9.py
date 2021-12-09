def read_file():
    heights = []
    test = """2199943210
    3987894921
    9856789892
    8767896789
    9899965678"""
    with open("input_day9.txt", "r") as input_file:
        for line in input_file:
            heights.append([int(i) for i in line.strip()])
    return heights


def is_low(heights, row, column):
    point = heights[row][column]
    if row + 1 < len(heights):
        if heights[row + 1][column] <= point:
            return False
    if row > 0:
        if heights[row - 1][column] <= point:
            return False
    if column + 1 < len(heights[0]):
        if heights[row][column + 1] <= point:
            return False
    if column > 0:
        if heights[row][column - 1] <= point:
            return False
    return True


def find_lowests(heights):
    lowests = []
    low_coords = []
    for row in range(len(heights)):
        for column in range(len(heights[0])):
            if is_low(heights, row, column):
                lowests.append(heights[row][column])
                low_coords.append([row, column])
    print(sum(lowests) + len(lowests))
    return low_coords


def right(heights, r, c, basin):
    if c + 1 < len(heights[r]) and heights[r][c + 1] > heights[r][c] and heights[r][c + 1] != 9:
        if [r, c + 1] not in basin:
            basin.append([r, c + 1])
            basin = check(heights, r, c + 1, basin)
    return basin


def up(heights, r, c, basin):
    if r - 1 >= 0 and heights[r - 1][c] > heights[r][c] and heights[r - 1][c] != 9:
        if [r - 1, c] not in basin:
            basin.append([r - 1, c])
            basin = check(heights, r - 1, c, basin)
    return basin


def down(heights, r, c, basin):
    if r + 1 < len(heights) and heights[r + 1][c] > heights[r][c] and heights[r + 1][c] != 9:
        if [r + 1, c] not in basin:
            basin.append([r + 1, c])
            basin = check(heights, r + 1, c, basin)
    return basin


def left(heights, r, c, basin):
    if c - 1 >= 0 and heights[r][c - 1] > heights[r][c] and heights[r][c - 1] != 9:
        if [r, c - 1] not in basin:
            basin.append([r, c - 1])
            basin = check(heights, r, c - 1, basin)
    return basin


def check(heights, r, c, basin):
    basin = left(heights, r, c, basin)
    basin = right(heights, r, c, basin)
    basin = up(heights, r, c, basin)
    basin = down(heights, r, c, basin)
    return basin


def find_all_basins(heights, low_coords):
    basins = []
    for r, c in low_coords:
        basins.append(check(heights, r, c, [[r, c]]))
    return basins


def three_biggest(basins):
    sizes = [len(b) for b in basins]
    sizes_temp = [a for a in sizes]
    biggest_sizes = []
    for _ in range(3):
        biggest_sizes.append(max(sizes_temp))
        sizes_temp.remove(max(sizes_temp))
    print(biggest_sizes)
    return biggest_sizes[0] * biggest_sizes[1] * biggest_sizes[2]


def main():
    hs = read_file()
    print(hs)
    lc = find_lowests(hs)
    print(lc)
    bas = find_all_basins(hs, lc)
    print(three_biggest(bas))


if __name__ == '__main__':
    main()
