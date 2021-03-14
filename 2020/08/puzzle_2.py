with open("input.txt") as input_file:
    instructions_list = input_file.read().split("\n")


def does_program_terminate():
    accumulator = 0
    program_counter = 0
    executed_instructions = []
    instruction = ""

    while True:
        if program_counter == len(instructions_list):
            print("Program terminated at instruction {0}. Accumulator value is {1}".format(instruction, accumulator))
            return True

        instruction = instructions_list[program_counter].split()
        operation = instruction[0]
        argument = int(instruction[1])

        if program_counter in executed_instructions:
            # print("Executed instruction {0} at line {1} a second time.".format(instruction, program_counter + 1))
            # print("Accumulator's value is " + str(accumulator))
            return False

        executed_instructions.append(program_counter)

        if operation == "acc":
            accumulator += argument
        elif operation == "jmp":
            program_counter += argument
            continue
        elif operation == "nop":
            pass

        program_counter += 1


for i in range(0, len(instructions_list)):
    instruction = instructions_list[i].split()
    operation = instruction[0]
    argument = instruction[1]

    if operation == "jmp":
        print("Changed line {0} {1} to nop".format(i + 1, instruction))
        instructions_list[i] = "nop " + argument
        if not does_program_terminate():
            instructions_list[i] = "jmp " + argument
        else:
            break
    elif operation == "nop":
        print("Changed line {0} {1} to jmp".format(i + 1, instruction))
        instructions_list[i] = "jmp " + argument
        if not does_program_terminate():
            instructions_list[i] = "nop " + argument
        else:
            break
