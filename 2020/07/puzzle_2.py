import re

with open("input.txt") as input_file:
    rules = input_file.read().split("\n")

regex = re.compile("^([a-z ]+) contain ([0-9a-z,. ]+).$")
bags_dic = {}

for rule in rules:
    outer_bag = regex.match(rule).group(1).rstrip('s')
    inner_bags = list(map(lambda x: x.rstrip('s'), regex.match(rule).group(2).split(",")))
    # The following code transforms e.g "3 blue bags" into {"blue bag": 3}, making a list of the contents for each bag
    for i in range(0, len(inner_bags)):
        bag = inner_bags[i].strip()
        if any(char.isdigit() for char in bag):
            inner_bags[i] = {bag.lstrip(bag[0]).strip(): bag[0]}
    bags_dic.update({outer_bag: inner_bags})


def bags_inside(bag_colour):
    total = 0
    inside_bags = bags_dic[bag_colour]
    if 'no other bag' in inside_bags:
        # print("No bag in " + bag_colour)
        return 0
    for b in inside_bags:
        k = list(b.items())[0][0]       # The colour of the bag
        v = int(list(b.items())[0][1])  # How many of it is in the current bag being inspected (function argument)
        # print("Checking for {0} {1}s inside {2}: {3}".format(v, k, bag_colour, inside_bags))
        total += v + (v * bags_inside(k))
    return total


all_total = bags_inside('shiny gold bag')
print(all_total)
