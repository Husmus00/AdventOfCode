import re

with open("input.txt") as input_file:
    program = input_file.read().splitlines()

mask = ''
memory = {}


def apply_mask(dec_value):
    # Convert decimal value to binary string and pad left with zeros so length is 36
    # Then convert string to list since strings do not support setitem
    bin_string = list(bin(dec_value).replace("0b", "").rjust(36, '0'))

    for i in range(0, len(mask)):
        if mask[i] != 'X':
            bin_string[i] = mask[i]

    dec_value = int("".join(bin_string), 2)
    return dec_value


def parse(operation):
    operation = re.search(r"mem\[([0-9]+)] = ([0-9]+)", operation)
    a = operation.group(1)
    v = apply_mask(int(operation.group(2)))
    return a, v


for line in program:
    if line.startswith("mask"):
        mask = line.strip("mask = ")
        continue

    address, value = parse(line)
    # print("{}, {}".format(address, value))
    memory[address] = value

total = 0
for v in memory.values():
    total += v

print(total)
