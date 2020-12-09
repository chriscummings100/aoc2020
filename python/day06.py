unique = sum([len(set(list(x.replace("\n","")))) for x in open("day06input.txt").read().split("\n\n") ])
print(f"PartA: {unique}")

unique = sum([len(set.intersection(*[set(list(passenger)) for passenger in filter(None,group.split("\n"))])) for group in open("day06input.txt").read().split("\n\n")])
print(f"PartB: {unique}")

