example_data = """\
16
10
15
5
1
11
7
19
6
12
4"""

example_data = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

with open("day10input.txt") as f:
    data = f.read()


data = example_data

data = [0] + [int(x) for x in data.splitlines()]
sorted_data = sorted(data)
sorted_data.append(sorted_data[-1]+3)

dist = [0,0,0,0]

for i in range(1, len(sorted_data)):
    dist[sorted_data[i] - sorted_data[i-1]] += 1


mult = dist[1] * dist[3]

print(f"PartA: {mult}")

paths = [0 for x in sorted_data]
paths[0] = 1

for i in range(1,len(sorted_data)):
    for j in range(max(i-3,0),i):
        delta = sorted_data[i] - sorted_data[j]
        if delta <= 3:
            paths[i] += paths[j]
        
print(paths)


