def read_file():
    values = []
    with open("input_day6.txt", "r") as input_file:
        values = [int(i) for i in input_file.readline().strip().split(",")]
    return values


def progress(model):
    start_len = len(model)
    for i in range(start_len):
        if model[i] == 0:
            model[i] = 6
            model.append(8)
        else:
            model[i] -= 1
    return model


def after_days(model, days):
    for day in range(days):
        model = progress(model)
        # print(day,model)
    return model


def calculate(model, days):
    first_grows = [0, 0, 0, 0, 0, 0, 0]
    waiting = [[0, 0] for _ in first_grows]

    for fish in model:
        first_grows[fish] += 1

    # for i in range(days):
    #     print("b", i, first_grows, waiting)
    #     first_grows[i % 7] += waiting[i % 7][0]
    #     waiting[i % 7][0] = waiting[i % 7][1]
    #     waiting[(i + 1) % 7][1] = first_grows[i % 7]
    #     print("a", day % 7, first_grows, waiting)

    to_add_on_days = {}

    for day in range(days):
        amount_adding = first_grows[day % 7]
        add_on_day = day + 8
        to_add_on_days[add_on_day] = amount_adding

        if day in to_add_on_days.keys():
            first_grows[(day+1) % 7] += to_add_on_days[day]
            to_add_on_days.pop(day)

        # print(day, first_grows, to_add_on_days)
    print(sum(first_grows)+ sum(to_add_on_days.values()))


if __name__ == '__main__':
    fish_model = read_file()
    print(len(after_days(fish_model, 80)))
    fish_model = read_file()
    calculate(fish_model, 256)
