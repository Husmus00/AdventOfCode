"""
--- Day 18: Operation Order ---

As you look out the window and notice a heavily-forested continent slowly appear over the horizon,
you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (
*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated
before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the
operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition,
the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71

Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) +
(4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51

Here are a few more examples:

    2 * 3 + (4 * 5) becomes 26.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of
the homework; what is the sum of the resulting values?
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
            elif buffer == "+" or buffer == "*":
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
