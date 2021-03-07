"""
--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which
everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c,
    they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""

with open("input.txt") as input_file:
    # Seperate input into a list where each element is a list of a single group's answers
    answers = list(map(lambda x: x.split("\n"), input_file.read().split("\n\n")))

# The logic here is that, in every group, for each letter in the first person's answer that exists in every other
# person's answer, that letter should be counted. No need to check for each letter in the other people's answers, if
# it didn't exist in the first person's answer, then not everyone answered that letter.

print(answers)

total_sum = 0

for a in answers:
    if len(a) == 1:
        total_sum += len(a[0])
    else:
        first_person = a[0]
        for letter in first_person:
            all_answered_letter = list(map(lambda x: letter in x, a))
            print(all_answered_letter)
            if all_answered_letter.count(True) == len(all_answered_letter):
                # every element is True
                total_sum += 1
    print(total_sum)

print(total_sum)
