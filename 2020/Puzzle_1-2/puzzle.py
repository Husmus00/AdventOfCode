"""
https://adventofcode.com/2020/day/1

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from
a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same
criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together
produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""

with open("input.txt") as input_file:
    numbers = input_file.readlines()

    index = 0
    for n in numbers:
        numbers[index] = int(numbers[index].replace("\n", ""))
        index = index + 1

print(numbers)

found = False  # in order to break from the while loop when found
tested = 0  # the number of entries tested
first_number = 0
second_number = 0
third_number = 0
result_multiplied = 0

"""
while tested < len(numbers) and found is False:
    entry_to_test = numbers[tested]
    index = 0

    print(tested)

    for n in numbers:
        addition = entry_to_test + numbers[index]
        if addition == 2020:
            first_number = entry_to_test
            second_number = numbers[index]
            result_multiplied = first_number * second_number
            found = True
            break

        index = index + 1
    tested = tested + 1
"""

while not found and tested < len(numbers):
    index_two = 0
    entry_one = numbers[tested]

    for entry_two in numbers:
        index_three = 0
        for entry_three in numbers:

            addition = entry_one + entry_two + entry_three

            print("At {0}, {1}, {2} : {3}".format(tested, index_two, index_three, addition))

            if addition == 2020:
                print("FOUND")
                first_number = entry_one
                second_number = entry_two
                third_number = entry_three
                result_multiplied = first_number * second_number * third_number
                found = True

            index_three = index_three + 1

        index_two = index_two + 1

    tested = tested + 1

print(first_number + second_number + third_number)
print(str(first_number) + " * " + str(second_number) + " * " + str(third_number) + " = " + str(result_multiplied))
