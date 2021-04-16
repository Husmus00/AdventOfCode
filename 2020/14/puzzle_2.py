# Answer by evqna

with open("input.txt") as input_file:
    program = input_file.read()


def recursive_replace(floating_addr):
    if 'X' not in floating_addr:
        return [int(floating_addr, 2)]

    L = recursive_replace(floating_addr.replace('X', '0', 1))
    L += recursive_replace(floating_addr.replace('X', '1', 1))
    return L


def write(mem, addr, mask, val):
    addr = addr | int(mask.replace('X', '0'), 2)
    floating_repr = list(format(addr, '0=36b'))  # Fixed 36-bit binary output with 0-padding
    for i, c in enumerate(mask):
        if c == 'X':
            floating_repr[i] = 'X'
    floating = ''.join(floating_repr)

    for dest in recursive_replace(floating):
        mem[dest] = val


def run(s):
    instructions = s.splitlines()

    mem = {}
    mask = ''
    for ins in instructions:
        op, val = ins.split(' = ')
        if op.startswith('mem'):
            addr = int(op[4:-1])
            write(mem, addr, mask, int(val))
        elif op.startswith('mask'):
            mask = val

    print(sum(mem.values()))
    return sum(mem.values())


run(program)
