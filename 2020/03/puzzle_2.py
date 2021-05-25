"""
--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner
and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce
the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

# My plan is as follows: the "lines" array will contain each line (row) and will represent the y-plane
# each string (row) will represent the x-plane with each index in the string a coordinate in the x-plane
# since the map loops around in the x-direction infinitely the x-coordinate must loop around when it exceeds the length
# of the map in the x-direction.
# Thus, lines[y_coordinate][x_coordinate] will represent whatever is at x, y on the map (either . or #)

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def number_of_trees(slope_x, slope_y):
    x_coordinate = 0
    y_coordinate = 0
    trees = 0

    for l in lines:
        x_coordinate = (x_coordinate + slope_x) % len(l)  # loop around the horizontal plane
        y_coordinate += slope_y

        if y_coordinate < len(lines):
            location = lines[y_coordinate][x_coordinate]
            if location == '#':
                trees += 1

    print("Number of trees: " + str(trees))
    return trees


trees_multiplied = 1  # not 0 because multiplying by 0 will always result in 0 (I made a mistake)

for s in slopes:
    trees_multiplied *= number_of_trees(s[0], s[1])

print("Number of trees multiplied: " + str(trees_multiplied))
