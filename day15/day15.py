import heapq


class Node:
    def __init__(self, x, y, previous, distance, edge_weight):
        self.x = x
        self.y = y
        self.previous = previous
        self.distance = distance
        self.edge_weight = edge_weight

    def update(self, previous):
        new_dist = self.edge_weight + previous.distance
        if new_dist < self.distance:
            # print("{} = {} + {}".format(new_dist, self.edge_weight, previous.distance))
            # print("nn = {},{} + {},{}".format(self.x, self.y, previous.x, previous.y))
            self.distance = new_dist
            self.previous = previous

    def adjacent_to_check(self, dist, unvisited):
        to_check = []
        if self.x > 0:
            left = dist[self.y][self.x - 1]
            if left in unvisited:
                to_check.append(left)
        if self.x < len(dist[0]) - 1:
            right = dist[self.y][self.x + 1]
            if right in unvisited:
                to_check.append(right)
        if self.y > 0:
            up = dist[self.y - 1][self.x]
            if up in unvisited:
                to_check.append(up)
        if self.y < len(dist) - 1:
            down = dist[self.y + 1][self.x]
            if down in unvisited:
                to_check.append(down)
        return to_check


def read_file():
    values = []
    with open("input_day15.txt", "r") as input_file:
        for line in input_file:
            values.append([int(i) for i in line.strip()])
    return values


def initial_distances(values):
    dist = []
    for row in range(len(values)):
        dist.append([])
        for col in range(len(values[0])):
            if row == 0 and col == 0:
                dist[row].append(Node(col, row, 'self', 0, values[row][col]))
            else:
                dist[row].append(Node(col, row, None, float('inf'), values[row][col]))
    unvisited = []
    for row in dist:
        for item in row:
            unvisited.append(item)
    return dist, unvisited


def min_node(unvisited):
    min_dist = min(unvisited, key=lambda n: n.distance)
    return min_dist


def path(values):
    visited = []
    dist, unvisited = initial_distances(values)
    current_min = min_node(unvisited)
    while current_min.y != len(dist) - 1 or current_min.x != len(dist[0]) - 1:
        current_min = min_node(unvisited)

        visited.append(current_min)
        unvisited.remove(current_min)
        for node in current_min.adjacent_to_check(dist, unvisited):
            # print("update", node.x, node.y, node.distance)
            node.update(current_min)
    path_last = current_min
    while path_last.previous != 'self':
        # print(path_last.x, path_last.y, path_last.distance)
        path_last = path_last.previous
    # print(path_last.x, path_last.y, path_last.distance)
    for row in dist:
        print([node.distance for node in row])


def make_new_tile(old_tile, add):
    new_tile = []
    for r in range(len(old_tile)):
        new_tile.append([])
        for i in range(len(old_tile[r])):
            new_tile[r].append(((old_tile[r][i] + add) - 1) % 9 + 1)
    return new_tile


def tile_together(first, second, x):
    if not x:
        return first + second
    else:
        return [first[i] + second[i] for i in range(len(first))]


def tile_values(values, x, y):
    expand = [r.copy() for r in values]
    for x_add in range(1, x):
        expand = tile_together(expand, make_new_tile(values, x_add), True)
    expand_y = [r.copy() for r in expand]
    for y_add in range(1, y):
        expand_y = tile_together(expand_y, make_new_tile(expand, y_add), False)
    return expand_y


def main():
    values = read_file()
    # for v in values:
    #     print(v)
    dist = initial_distances(values)
    # for r in dist:
    #     print([d.distance for d in r])
    # path(values) # part 1
    # print(tile_together(values, make_new_tile(values, 1), True))
    tiled = tile_values(values, 5, 5)
    # for t in tiled:
    #     print("".join(str(v) for v in t))
    path(tiled)


if __name__ == '__main__':
    main()
