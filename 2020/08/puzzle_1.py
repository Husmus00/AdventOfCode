with open("input.txt") as input_file:
    instructions_list = input_file.read().split("\n")

accumulator = 0
program_counter = 0
executed_instructions = []

while True:
    instruction = instructions_list[program_counter].split()
    operation = instruction[0]
    argument = int(instruction[1])

    if program_counter in executed_instructions:
        print("Executed instruction {0} at line {1} a second time.".format(instruction, program_counter))
        print("Accumulator's value is " + str(accumulator))
        break

    executed_instructions.append(program_counter)

    if operation == "acc":
        accumulator += argument
    elif operation == "jmp":
        program_counter += argument
        continue
    elif operation == "nop":
        pass

    program_counter += 1
