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


if __name__ == '__main__':
    original_values = read_file()
    counted_values = count_0s_and_1s(original_values)
    gamma, epsilon = find_gamma(counted_values)
    gamma_int = bin_list_to_int(gamma)
    epsilon_int = bin_list_to_int(epsilon)
    print(gamma_int*epsilon_int)
