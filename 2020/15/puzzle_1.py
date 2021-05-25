with open("input.txt") as input_file:
    starting_numbers = input_file.read().strip("\n").split(",")

mentioned_at = {}
turn = 0
prev_num = 0

# intialize
for i, n in enumerate(starting_numbers):
    n = int(n)
    turn += 1
    mentioned_at[n] = turn
    prev_num = n

prev_num = 0  # first number spoken after starting numbers is always 0


def next_spoken():
    if prev_num in mentioned_at:
        return turn - mentioned_at[prev_num]
    else:
        return 0


while turn < 30000000:
    turn += 1
    next_num = next_spoken()
    mentioned_at[prev_num] = turn
    if turn == 30000000 - 1:
        print("Turn {}, Spoken {}".format(turn, next_num))
    prev_num = next_num
