from functools import reduce


def read_file():
    with open("input_day16.txt", "r") as input_file:
        value = input_file.readline()
    return value


def to_binary(hex_value):
    bin_value = ""
    for char in hex_value:
        bin_value += str(bin(int(char, 16)))[2:].zfill(4)
    return bin_value


def literal(bin_value, place):
    end = place
    number = ""
    while end < len(bin_value) and (end == place or bin_value[end - 5] != '0'):
        number += bin_value[end + 1:end + 5]
        end += 5
    return end, int(number, 2)


def operator(bin_value, place):
    return place


def version_next(bin_value, place, total):
    if place >= len(bin_value):
        return total
    packet_version = bin_value[place:place + 3]
    place += 3
    packet_type = bin_value[place:place + 3]
    place += 3
    if packet_type == 4:  # literal
        place = literal(packet_version, place)
        total += packet_version
    else:  # operator
        place = operator(packet_version, place)
        total += packet_version
    return version_next(bin_value, place, total)


def parse_packet(bin_value, pointer, total):
    version = bin_value[pointer:pointer + 3]
    pointer += 3

    total += int(version, 2)

    type_id = bin_value[pointer:pointer + 3]
    pointer += 3

    if type_id == '100':  # literal
        pointer, value = literal(bin_value, pointer)
        return pointer, total, value
    else:
        length_type_id = bin_value[pointer]
        pointer += 1

        operation_values = []

        if length_type_id == '0':
            num_bits = int(bin_value[pointer:pointer + 15], 2)
            pointer += 15

            packet_start = pointer

            while pointer < packet_start + num_bits:
                pointer, total, value = parse_packet(bin_value, pointer, total)
                operation_values.append(value)

        if length_type_id == '1':
            child_count = int(bin_value[pointer:pointer + 11], 2)
            pointer += 11

            for _ in range(child_count):
                pointer, total, value = parse_packet(bin_value, pointer, total)
                operation_values.append(value)

        if type_id == '000':
            return pointer, total, sum(operation_values)
        elif type_id == "001":
            return pointer, total, reduce(lambda x, y: x * y, operation_values)
        elif type_id == "010":
            return pointer, total, min(operation_values)
        elif type_id == "011":
            return pointer, total, max(operation_values)
        elif type_id == "101":
            return pointer, total, 1 if operation_values[0] > operation_values[1] else 0
        elif type_id == "110":
            return pointer, total, 1 if operation_values[0] < operation_values[1] else 0
        else:
            return pointer, total, 1 if operation_values[0] == operation_values[1] else 0


def main():
    hex_value = read_file()
    bin_value = to_binary(hex_value)
    print(parse_packet(bin_value, 0, 0))


if __name__ == '__main__':
    main()
