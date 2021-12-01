def list_read():
    depth_list = []
    with open("day1/input_day1.txt", "r") as list_input:
        for line in list_input:
            depth_list.append(int(line.strip()))
    return depth_list


def increase_count(depth_list):
    count = 0
    for i in range(1, len(depth_list)):
        if depth_list[i] > depth_list[i - 1]:
            count += 1
    return count


def sum_windows(depth_list):
    sums = []
    for i in range(2, len(depth_list)):
        sums.append(depth_list[i] + depth_list[i - 1] + depth_list[i - 2])
    return sums


def sliding_increase(depth_list):
    return increase_count(sum_windows(depth_list))


def main():
    depth_list = list_read()
    print(increase_count(depth_list))
    print(sliding_increase(depth_list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
