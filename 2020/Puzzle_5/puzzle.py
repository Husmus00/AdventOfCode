"""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours
, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input);
perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like
FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through
127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first
letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates
which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane
(numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the
lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.

So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID
44 * 8 + 5 = 357.

Here are some other boarding passes:

    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a
catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing
from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""

# Part 1

with open("input.txt") as input_file:
    boarding_passes = input_file.read().split("\n")

highest_ID = 0
smallest_ID = 1000  # For part 2, 1000 is an arbitrary "safe" number
list_of_IDs = []    # For part 2

for bp in boarding_passes:
    row = [0, 128]   # "Upper bound" is non-inclusive
    column = [0, 8]  # Same here

    # first 7 characters (row)
    for index in range(7):
        character = bp[index]
        if character == 'F':
            row = [row[0], int((row[1] - row[0]) / 2) + row[0]]
            # print("Letter is F and row is now " + str(row))
        if character == 'B':
            row = [int((row[1] - row[0]) / 2) + row[0], row[1]]
            # print("Letter is B and row is now " + str(row))
    row = row[0]  # At the end, the lower bound is always the number we want

    # last 3 characters (column)
    for index in range(7, 10):
        character = bp[index]
        if character == 'L':
            column = [column[0], int((column[1] - column[0]) / 2) + column[0]]
            # print("Letter is L and row is now " + str(row))
        if character == 'R':
            column = [int((column[1] - column[0]) / 2) + column[0], column[1]]
            # print("Letter is R and row is now " + str(row))
    column = column[0]  # At the end, the lower bound is always the number we want

    seat_ID = row * 8 + column
    if seat_ID > highest_ID:
        highest_ID = seat_ID

    if seat_ID < smallest_ID:
        smallest_ID = seat_ID

    list_of_IDs.append(seat_ID)

    # print("Row is {0}, Column is {1}, Seat ID is {2}".format(row, column, seat_ID))

print("Highest ID is {0} and smallest ID is {1}".format(highest_ID, smallest_ID))

# Part 2

list_of_IDs.sort()
counter = smallest_ID  # we start comparing from the smallest ID

# Here we compare value at the index to the "counter" to find the missing number
for i in range(len(list_of_IDs)):
    if counter != list_of_IDs[i]:
        print("My ID is " + str(counter))
        break
    counter = counter + 1
