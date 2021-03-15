"""
--- Part Two ---

After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc
instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction
in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop,
never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually
find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The
instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last
instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc
+1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the
value of the accumulator after the program terminates? """

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
