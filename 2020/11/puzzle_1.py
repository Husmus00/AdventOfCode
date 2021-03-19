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
    adjacent_seat_coordinates = [
        [x - 1, y - 1], [x - 1, y], [x - 1, y + 1],  # Above row
        [x, y - 1], [x, y + 1],                      # current row
        [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]   # Below row
    ]

    for s in adjacent_seat_coordinates:
        if -1 < s[0] < len(current_state) and -1 < s[1] < len(current_state[s[0]]):
            adjacent_seat = current_state[s[0]][s[1]]
            if adjacent_seat == '#':
                count += 1

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
            elif seat == '#' and occupied_neighbors >= 4:
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

