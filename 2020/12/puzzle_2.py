with open("input.txt") as input_file:
    instructions = input_file.read().split("\n")

# This solution is highly convoluted and using 2 values for the boat's position
# and 2 values for the waypoint position would be cleaner

mapping = ['E', 'S', 'W', 'N']
directions = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
waypoint = ['E', 10, 'N', 1]

for i in instructions:
    action, value = i[0], int(i[1:])

    if action == 'F':
        directions[waypoint[0]] += value * waypoint[1]
        directions[waypoint[2]] += value * waypoint[3]
        # print("Forward {0}, direction {1}".format(value, facing))
    elif action == 'R':
        rotations = int(value / 90)
        waypoint[0] = mapping[(mapping.index(waypoint[0]) + rotations) % 4]
        waypoint[2] = mapping[(mapping.index(waypoint[2]) + rotations) % 4]
        # print("Right {0}. Rotations {1}. Direction now {2}".format(value, rotations, facing))
    elif action == 'L':
        rotations = int(value / 90)
        waypoint[0] = mapping[(mapping.index(waypoint[0]) - rotations) % 4]
        waypoint[2] = mapping[(mapping.index(waypoint[2]) - rotations) % 4]
        # print("Left {0}. Rotations {1}. Direction now {2}".format(value, rotations, facing))
    else:
        if action == 'N' or action == 'S':
            if action == 'N' and 'N' in waypoint:
                waypoint[waypoint.index('N') + 1] += value
            elif action == 'N' and 'S' in waypoint:
                waypoint[waypoint.index('S') + 1] -= value
            elif action == 'S' and 'N' in waypoint:
                waypoint[waypoint.index('N') + 1] -= value
            elif action == 'S' and 'S' in waypoint:
                waypoint[waypoint.index('S') + 1] += value
        elif action == 'E' or action == 'W':
            if action == 'E' and 'E' in waypoint:
                waypoint[waypoint.index('E') + 1] += value
            elif action == 'E' and 'W' in waypoint:
                waypoint[waypoint.index('W') + 1] -= value
            elif action == 'W' and 'E' in waypoint:
                waypoint[waypoint.index('E') + 1] -= value
            elif action == 'W' and 'W' in waypoint:
                waypoint[waypoint.index('W') + 1] += value
        # print("{0} {1}".format(action, value))

north_south = abs(directions['N'] - directions['S'])
east_west = abs(directions['E'] - directions['W'])
print("Manhattan distance: {0}".format(north_south + east_west))
