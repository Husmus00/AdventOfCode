with open("example_1.txt") as input_file:
    sn = input_file.read()


def get_next_number(prev, state, ts):
    if prev not in state:
        return 0
    return ts - state[prev]


def run(s):
    starting_numbers = [int(c) for c in s.strip().split(',')]
    game_state = {n: i + 1 for i, n in enumerate(starting_numbers)}
    print(game_state)

    round_num = len(starting_numbers) + 1
    cur = 0
    while round_num < 10:
        next = get_next_number(cur, game_state, round_num)
        print("Round {}, {}".format(round_num, next))
        game_state[cur] = round_num
        cur = next
        round_num += 1
    return cur


print(run(sn))
