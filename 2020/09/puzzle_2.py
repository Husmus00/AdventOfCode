"""
--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous
set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course,
the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example,
these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""

with open("input.txt") as input_file:
    numbers = input_file.read().split("\n")

print(numbers)
twenty_five = []
invalid_number = 0


# Get the invalid number
# ----------------------
def shift_numbers(new_number):
    del twenty_five[0]
    twenty_five.append(new_number)


for i in range(0, len(numbers)):
    # Preamble
    if i < 25:
        twenty_five.append(numbers[i])
        continue

    number_to_check = int(numbers[i])
    found = False
    for j in twenty_five:
        for k in twenty_five:
            if number_to_check == int(j) + int(k):
                found = True

    if found is False:
        invalid_number = number_to_check
        print("Invalid number is {0} at line {1}".format(invalid_number, i + 1))
        break

    shift_numbers(number_to_check)


# Part 2
# ------

def sum_min_max(valid_list):
    min_max = min(valid_list) + max(valid_list)
    print("Valid list is {0} and sum of min and max is {1}".format(valid_list, min_max))


for i in range(0, len(numbers)):
    contiguous_list = [int(numbers[i])]  # Pre-populate the list with the first number
    j = i + 1
    while j < len(numbers):
        contiguous_list.append(int(numbers[j]))
        cont_sum = sum(contiguous_list)

        if cont_sum < invalid_number:
            j += 1
            continue
        elif cont_sum == invalid_number:
            sum_min_max(contiguous_list)
            break
        else:
            # Contiguous list is invalid
            break
