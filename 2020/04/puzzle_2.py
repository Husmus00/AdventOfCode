"""
--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are
getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules.
Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as
optional. In your batch file, how many passports are valid?
"""

import re

with open("input.txt") as input_file:
    passports = input_file.read().split("\n\n")

accepted_tags = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
accepted_tags.sort()


def valid_passports():
    valid = 0

    for p in passports:
        fields = p.split()
        tags = []

        for f in fields:
            tag = f.split(':')[0]
            value = f.split(':')[1]
            if field_is_valid(tag, value):
                print("(tag {}: value {}) is valid".format(tag, value))
                tags.append(tag)
            else:
                print("(tag {}: value {}) is invalid".format(tag, value))

        tags.sort()
        if tags == accepted_tags:
            valid += 1

        print("\n")

    return valid


def field_is_valid(tag, value):
    if tag == 'byr' and len(value) == 4 and 1920 <= int(value) <= 2002:
        return True

    elif tag == 'iyr' and len(value) == 4 and 2010 <= int(value) <= 2020:
        return True

    elif tag == 'eyr' and len(value) == 4 and 2020 <= int(value) <= 2030:
        return True

    elif tag == 'hgt':
        height = int(re.match(r'\d+', value, flags=0).group(0))  # use regex to extract height

        if re.match(r'^\d+cm$', value, flags=0) and 150 <= height <= 193:  # height is in cm
            return True
        elif re.match(r'^\d+in$', value, flags=0) and 59 <= height <= 76:
            return True

    elif tag == 'hcl' and re.match(r'#[0-9a-f]{6}', value, flags=0):
        return True

    elif tag == 'ecl':
        eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        if value in eye_colours:
            return True

    elif tag == 'pid':
        print(value)

        # leading_zeros = ''
        remainder_of_id = ''
        # if re.match(r'^0+', value, flags=0):
        # leading_zeros = re.match(r'^0+', value, flags=0).group(0)
        if re.match(r'^\d+$', value, flags=0):
            remainder_of_id = re.match(r'^\d+$', value, flags=0).group(0)

        # Test
        # if leading_zeros + remainder_of_id != value:
        #     print("ERROR")

        if len(remainder_of_id) == 9:
            return True

    else:
        return False


print("{} passports in list. Valid passports: {}".format(len(passports), str(valid_passports())))
