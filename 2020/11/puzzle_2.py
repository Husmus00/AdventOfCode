import copy

with open("input.txt") as input_file:
    current_state = list(map(lambda x: list(x), input_file.read().split("\n")))

next_state = []


def print_current_state():
    for row in range(0, len(current_state)):
        for r in current_state[row]:
            print(r, end="")
        print()
    print()


def current_occupied_neighbors(x, y):
    count = 0
    # Check in each of the eight directions for the first seat
    check_x = 0
    check_y = 0
    # Top
    check_x = x - 1
    check_y = y
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_x -= 1
                continue
            elif seat == '#':
                count += 1
        break
    # Top left
    check_x = x - 1
    check_y = y - 1
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_x -= 1
                check_y -= 1
                continue
            elif seat == '#':
                count += 1
        break
    # Top right
    check_x = x - 1
    check_y = y + 1
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_x -= 1
                check_y += 1
                continue
            elif seat == '#':
                count += 1
        break
    # Left
    check_x = x
    check_y = y - 1
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_y -= 1
                continue
            elif seat == '#':
                count += 1
        break
    # Right
    check_x = x
    check_y = y + 1
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_y += 1
                continue
            elif seat == '#':
                count += 1
        break
    # Bottom
    check_x = x + 1
    check_y = y
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_x += 1
                continue
            elif seat == '#':
                count += 1
        break
    # Bottom left
    check_x = x + 1
    check_y = y - 1
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_x += 1
                check_y -= 1
                continue
            elif seat == '#':
                count += 1
        break
    # Bottom right
    check_x = x + 1
    check_y = y + 1
    while True:
        if -1 < check_x < len(current_state) and -1 < check_y < len(current_state[check_x]):
            seat = current_state[check_x][check_y]
            if seat == '.':
                check_x += 1
                check_y += 1
                continue
            elif seat == '#':
                count += 1
        break

    return count


def perform_round():
    for seat_x in range(0, len(current_state)):
        for seat_y in range(0, len(current_state[seat_x])):
            seat = current_state[seat_x][seat_y]

            if seat == '.':
                continue

            occupied_neighbors = current_occupied_neighbors(seat_x, seat_y)

            if seat == 'L' and occupied_neighbors == 0:
                next_state[seat_x][seat_y] = '#'
            elif seat == '#' and occupied_neighbors >= 5:
                next_state[seat_x][seat_y] = 'L'

            # print("Seat {0} at {1},{2} has {3} neighbors".format(seat, seat_x, seat_y, occupied_neighbors))


rounds = 0
while next_state != current_state:
    # while rounds < 3:

    if rounds == 0:
        next_state = copy.deepcopy(current_state)

    current_state = copy.deepcopy(next_state)

    print("Round " + str(rounds))
    print_current_state()
    perform_round()

    rounds += 1

all_occupied_seats = 0
for cs in current_state:
    all_occupied_seats += cs.count('#')
print(all_occupied_seats)
