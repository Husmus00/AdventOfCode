import re

with open("input.txt") as input_file:
    rules = input_file.read().split("\n")

regex = re.compile("^([a-z ]+) contain ([0-9a-z,. ]+).$")
bags_dic = {}
valid_bag_colours = []

for rule in rules:
    outer_bag = regex.match(rule).group(1).rstrip('s')
    inner_bags = list(map(lambda x: x.rstrip('s'), regex.match(rule).group(2).split(",")))
    # The following code is to remove the numbers from each bag (e.g "3 blue bags" -> "blue bag")
    for i in range(0, len(inner_bags)):
        bag = inner_bags[i].strip()
        if any(char.isdigit() for char in bag):
            inner_bags[i] = bag.lstrip(bag[0]).strip()
    bags_dic.update({outer_bag: inner_bags})

#

for bag in bags_dic:
    if 'shiny gold bag' in bags_dic[bag]:
        valid_bag_colours.append(bag)

# Still not sure what defines how many iterations we need to do
for i in range(0, 5):
    print(i)
    valid_bag_colours = list(set(valid_bag_colours))
    for bag in bags_dic:
        if any(b in bags_dic[bag] for b in valid_bag_colours):
            valid_bag_colours.append(bag)

valid_bag_colours = list(set(valid_bag_colours))
print(len(valid_bag_colours))