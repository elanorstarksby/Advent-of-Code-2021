def step(location, velocity):
    #     The probe's x position increases by its x velocity.
    # The probe's y position increases by its y velocity.
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    # Due to gravity, the probe's y velocity decreases by 1.
    new_location = (location[0] + velocity[0], location[1] + velocity[1])
    new_velocity = (velocity[0] - 1 if velocity[0] > 0 else (-1 if velocity[0] < 0 else 0), velocity[1] - 1)
    return new_location, new_velocity


def do_stuff(velocity, target_x, target_y):
    start_velocity = velocity
    location = (0, 0)
    max_height = 0
    while True:
        location, velocity = step(location, velocity)
        max_height = max(max_height, location[1])
        if target_x[0] <= location[0] <= target_x[1] and target_y[0] <= location[1] <= target_y[1]:
            print("in", start_velocity, max_height)
            return True
        if target_x[1] <= location[0] or target_y[0] >= location[1]:
            # print("missed")
            return False


def main():
    target_x = (265, 287)
    target_y = (-103, -58)
    count_in = 0
    for x_vel in range(1, 288):
        for y_vel in range(-104, 300):
            if do_stuff((x_vel, y_vel), target_x, target_y):
                count_in += 1
    print(count_in, "were in")


if __name__ == '__main__':
    main()
