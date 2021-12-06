def read_file():
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
    return model


def calculate(model, days):
    first_grows = [0, 0, 0, 0, 0, 0, 0]

    for fish in model:
        first_grows[fish] += 1

    to_add_on_days = {}

    for day in range(days):
        amount_adding = first_grows[day % 7]
        add_on_day = day + 8
        to_add_on_days[add_on_day] = amount_adding

        if day in to_add_on_days.keys():
            first_grows[(day+1) % 7] += to_add_on_days[day]
            to_add_on_days.pop(day)

        # print(day, first_grows, to_add_on_days)
    return sum(first_grows)+ sum(to_add_on_days.values())


if __name__ == '__main__':
    fish_model = read_file()
    print(len(after_days(fish_model, 80)))
    fish_model = read_file()
    print(calculate(fish_model, 256))
