def read_file():
    with open("input_day7.txt", "r") as input_file:
        values = [int(i) for i in input_file.readline().strip().split(",")]
    return values


def align_to(positions, target):
    fuel = 0
    for position in positions:
        fuel += abs(target - position)
    return fuel


def align_to_sumn(positions, target):
    fuel = 0
    for position in positions:
        n = abs(target - position)
        # S = n * (n + 1)/2
        fuel += n * (n+1) / 2
    return fuel


def find_least_fuel(positions):
    smallest = min(positions)
    biggest = max(positions)
    fuel = biggest*len(positions)
    for i in range(smallest, biggest+1):
        fuel = min(fuel, align_to(positions, i))
    return fuel


def find_least_fuel_sumn(positions):
    smallest = min(positions)
    biggest = max(positions)
    fuel = align_to_sumn(positions,smallest)
    # smallest_i = smallest
    for i in range(smallest, biggest+1):
        new = align_to_sumn(positions, i)
        if new < fuel:
            fuel = new
            # smallest_i = i
    return fuel


def main():
    positions = read_file()
    print(positions)
    print(find_least_fuel(positions))
    print(find_least_fuel_sumn(positions))

if __name__ == '__main__':
    main()