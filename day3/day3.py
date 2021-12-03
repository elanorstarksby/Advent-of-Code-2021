def read_file():
    values = []
    with open("input_day3.txt", "r") as input_file:
        for line in input_file:
            values.append([int(i) for i in line.strip()])
    return values


def count_0s_and_1s(values):
    count = [0 for _ in values[0]]
    # i = 0
    for reading in values:
        for r in range(len(reading)):
            count[r] += 1 if reading[r] == 1 else -1
    return count


def find_gamma(total_values):
    gammas = []
    epsilons = []
    for each in total_values:
        gammas.append(0 if each < 0 else 1)
        epsilons.append(1 if each < 0 else 0)
    return gammas, epsilons


def bin_list_to_int(bin_list):
    bin_list.reverse()
    total = 0
    multiplier = 1
    for each in bin_list:
        total += each * multiplier
        multiplier *= 2
    return total


def most_common_at(values, place):
    print(values, place)
    digits = []
    for each in values:
        digits.append(each[place])
    # print(digits)
    count1s = 0
    count0s = 0
    for each in digits:
        if each == 1:
            count1s += 1
        else:
            count0s += 1
    print(count0s, count1s)
    return -1 if count1s == count0s else 1 if count1s > count0s else 0


def matching(values, most_common):
    temp_values = []
    digit = 0
    while True:
        keep_digit = most_common_at(values, digit)
        if not most_common:
            if keep_digit == 0:
                keep_digit = 1
            elif keep_digit == 1:
                keep_digit = 0
        if keep_digit == -1:
            if most_common:
                keep_digit = 1
            else:
                keep_digit = 0
        # print(keep_digit)
        for value in values:
            if value[digit] == keep_digit:
                temp_values.append(value)

        digit += 1
        values, temp_values = temp_values, []
        if len(values) < 2:
            break
    # print(values)
    return values[0]


def match_digits(values2,mostleast):
    current_values = []
    for digit_place in range(len(values2[0])):
        if digit_place > 5:
            print(count_0s_and_1s(values2))
        keep_values = find_gamma(count_0s_and_1s(values2))[mostleast]
        if digit_place > 5:
            print(keep_values)
        for value in values2:
            if value[digit_place] == keep_values[digit_place]:
                current_values.append(value)
        values2, current_values = current_values, []
        if digit_place > 5:
            print(values2)
        # print(keep_values)
        if len(values2) == 1:
            break
    return values2[-1]


if __name__ == '__main__':
    original_values = read_file()
    counted_values = count_0s_and_1s(original_values)
    gamma, epsilon = find_gamma(counted_values)
    gamma_int = bin_list_to_int(gamma)
    epsilon_int = bin_list_to_int(epsilon)
    print(gamma_int*epsilon_int)
    # most_common = match_digits(original_values, 0)
    # oxygen = bin_list_to_int(most_common)
    # least_common = match_digits(original_values, 1)
    # co2 = bin_list_to_int(least_common)
    # print(oxygen * co2)
    least = matching(original_values, False)
    most = matching(original_values, True)
    print(bin_list_to_int(least) * bin_list_to_int(most))
