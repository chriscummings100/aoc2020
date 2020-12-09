
def seatid(val: str):
    rowid = int(val[0:7].replace("F","0").replace("B","1"), base=2)
    colid = int(val[7:10].replace("L","0").replace("R","1"), base=2)
    return rowid*8+colid

print(seatid("FBFBBFFRLR"))

lines = open("day05input.txt").readlines()

values = [seatid(x) for x in lines]

print(f"PartA: {max(values)}")

values.sort()

for i in range(1,len(values)):
    if (values[i-1]+1) != values[i]:
        print(values[i-1]+1)

#inoneline = max([
#        int(val.replace("F","0").replace("B","1").replace("L","0").replace("R","1"), base=2)
#        for val in open("day05input.txt").readlines()
#    ])
