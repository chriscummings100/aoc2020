

with open("../day01input.txt","r") as f:
    lines = [int(x) for x in f.readlines()]

print(lines)

for idx0 in range(0, len(lines)):
    for idx1 in range(idx0+1,len(lines)):
        for idx2 in range(idx1+1,len(lines)):
            val0 = lines[idx0]
            val1 = lines[idx1]
            val2 = lines[idx2]
            if (val0+val1+val2) == 2020:
                print(val0)
                print(val1)
                print(val2)
                print(val0*val1*val2)

