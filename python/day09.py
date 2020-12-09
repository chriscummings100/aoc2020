example_data = """\
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
576"""
example_preamble = 5

with open("day09input.txt") as f:
    data = f.read()
preamble = 25

#data = example_data
#preamble = example_preamble

data = [int(x) for x in data.splitlines()]

invalid_number = None

for index in range(preamble, len(data)):
    found = False
    for prev_index in range(index-preamble, index):
        for prev_index_2 in range(prev_index+1, index):
            tot = data[prev_index]+data[prev_index_2]
            if tot == data[index]:
                found = True
                break 
        if found:
            break
    if not found:
        invalid_number = data[index]
        break

print(f"Part A: {data[index]}")

code_number = None

for index in range(0, len(data)):
    total = data[index]
    smallest = data[index]
    biggest = smallest
    found = False

    for index_2 in range(index+1, len(data)):
        smallest = min(smallest, data[index_2])
        biggest = max(biggest, data[index_2])
        total += data[index_2]
        if total == invalid_number:
            found = True
            code_number = smallest + biggest

print(f"Part B: {code_number}")
