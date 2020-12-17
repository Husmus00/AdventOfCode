"""
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate
Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the
sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these
positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy
enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""

with open("input.txt") as input_files:
    passwords = input_files.read().splitlines()
    print(passwords)

valid = 0

for p in passwords:
    values = p.split()  # splits "4-5 m: mmpth" into ["4-5", "m:", "mmpth"]

    first_position = int(values[0].split('-')[0])  # will extract 4 from "4-5"
    second_position = int(values[0].split('-')[1])  # will extract 5 from "4-5"

    letter = values[1][0]  # will extract "m" from "m:"
    password = values[2]

    first_position_is_valid = password[first_position - 1] == letter
    second_position_is_valid = password[second_position - 1] == letter

    print("{}, {}, {}, {}, {}, {}".format(first_position, second_position, letter, password, first_position_is_valid,
                                          second_position_is_valid))

    if first_position_is_valid ^ second_position_is_valid:
        valid += 1

print(valid)
