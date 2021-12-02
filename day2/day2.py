def list_read():
    move_list = []
    with open("input_day2.txt", "r") as list_input:
        for line in list_input:
            move_list.append(line.strip().split(' '))
    return move_list


def directions(move_list):
    co_ords = [0, 0]
    for movement in move_list:
        if movement[0] == "forward":
            co_ords[0] += int(movement[1])
        elif movement[0] == "backwards":
            co_ords[0] -= int(movement[1])
        elif movement[0] == "down":
            co_ords[1] += int(movement[1])
        elif movement[0] == "up":
            co_ords[1] -= int(movement[1])
    return co_ords


def aim_directions(move_list):
    co_ords = {'f': 0, 'd': 0, 'a': 0}
    for movement in move_list:
        if movement[0] == "forward":
            co_ords['f'] += int(movement[1])
            co_ords['d'] += int(movement[1]) * co_ords['a']
        elif movement[0] == "down":
            co_ords['a'] += int(movement[1])
        elif movement[0] == "up":
            co_ords['a'] -= int(movement[1])
    return co_ords


if __name__ == '__main__':
    movements = list_read()
    print(movements)
    loc = aim_directions(movements)
    print(loc, loc['f'] * loc['d'])
