import re

example_data = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

with open("day07input.txt") as f:
    data = f.read()

#data = example_data

bags = {}

for line in data.splitlines():
    matches = re.match(r"^([\w\s]+) bags? contain (.*)\.$",line)
    container_col = matches.group(1)
    child_matches = re.findall(r"(\d+) ([\w\s]+) bags?", matches.group(2))
    bags[container_col] = child_matches

#for bag,children in bags.items():
#    print(bag)
#    print(children)

inputs = set(["shiny gold"])
all_outputs = set()
while len(inputs) > 0:
    outputs = set()
    for input_bag in inputs:
        for bag,children in bags.items():
            for bag_child in children:
                if bag_child[1] == input_bag:
                    outputs.add(bag)
    #print(outputs)
    all_outputs.update(outputs)
    inputs = outputs

print(f"PartA: {len(all_outputs)}")

all_bags = {}

def recurse_bags(bag_name, bag_count):
    bag = bags[bag_name]
    for child_pair in bag:
        child_name = child_pair[1]
        child_count = int(child_pair[0])
        child_count *= bag_count

        existing_count = all_bags.get(child_name, 0)
        existing_count += child_count
        all_bags[child_name] = existing_count

        recurse_bags(child_name, child_count)

recurse_bags("shiny gold", 1)

total = 0
for bag,count in all_bags.items():
    total += count

print(total)


