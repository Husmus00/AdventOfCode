"""
--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach
the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with.
Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231

Here are the other examples from above:

    1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
    2 * 3 + (4 * 5) becomes 46.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

What do you get if you add up the results of evaluating the homework problems using these new rules?
"""

with open("input.txt") as input_file:
    equations = input_file.read().strip().splitlines()


def solve(equation):
    first_operand = -1  # All numbers are positive so -1 is basically "null" here
    second_operand = -1
    operation = ""

    buffer = ""
    equation += " "  # This is so we can test for the last digit in the equation in absence of a parenthesis

    for i, c in enumerate(equation):
        # When encountering a space or parentheses, check if buffer is digit or operation and clear buffer
        if c == "(" or c == ")" or c == " ":
            if buffer.isdigit():
                if first_operand == -1:
                    first_operand = int(buffer)
                else:
                    second_operand = int(buffer)
                    break
            elif buffer == "+":
                operation = buffer
            elif buffer == "*":
                if "+" in equation:
                    first_operand = -1
                else:
                    operation = buffer

            buffer = ""
        else:
            buffer += c

    sub_equation = "{} {} {}".format(first_operand, operation, second_operand)
    solution = 0
    if operation == "+":
        solution = first_operand + second_operand
    elif operation == "*":
        solution = first_operand * second_operand
    else:
        print("operation error: " + operation)

    # The 1 in replace() is to prevent similar sub equations from being replaced (as the ordering here matters)
    equation = equation.replace(sub_equation, str(solution), 1).strip()  # Strip to remove the extra " " added above
    return equation


def reduce_parentheses(equation):
    left_parenth = 0
    right_parenth = 0
    for i, c in enumerate(equation):
        if c == '(':
            left_parenth = i
        elif c == ')':
            right_parenth = i
            break

    sub_equation = equation[left_parenth + 1: right_parenth]
    solution = solve(sub_equation)
    if solution.isdigit():
        # parentheses contained 2 operands and a single operation (remove parentheses)
        equation = equation.replace("(" + sub_equation + ")", str(solution))
    else:
        # parentheses contained several operands and operations (keep parentheses)
        equation = equation.replace(sub_equation, str(solution))

    return equation


total = 0
for eq in equations:
    # Iterate over equation and match a left parenthesis to a right one
    while '(' in eq:
        eq = reduce_parentheses(eq)

    while not eq.isdigit():
        eq = solve(eq)

    total = total + int(eq)

print("Total: " + str(total) + "\n")
