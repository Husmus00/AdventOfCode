with open("input.txt") as input_file:
    instructions = input_file.read().split("\n")

# A more elegant solution would involve setting the directions as x, y
# with x representing E/W and y representing N/S

mapping = ['E', 'S', 'W', 'N']  # map directions to indices
directions = {'E': 0, 'S': 0, 'W': 0, 'N': 0}
facing = 'E'

for i in instructions:
    action, value = i[0], int(i[1:])

    if action == 'F':
        directions[facing] += value
        # print("Forward {0}, direction {1}".format(value, facing))
    elif action == 'R':
        rotations = int(value / 90)
        facing = mapping[(mapping.index(facing) + rotations) % 4]
        # print("Right {0}. Rotations {1}. Direction now {2}".format(value, rotations, facing))
    elif action == 'L':
        rotations = int(value / 90)
        facing = mapping[(mapping.index(facing) - rotations) % 4]
        # print("Left {0}. Rotations {1}. Direction now {2}".format(value, rotations, facing))
    else:
        directions[action] += value
        # print("{0} {1}".format(action, value))

north_south = abs(directions['N'] - directions['S'])
east_west = abs(directions['E'] - directions['W'])
print("Manhattan distance: {0}".format(north_south + east_west))
