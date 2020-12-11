example_data = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

with open("day11input.txt") as f:
    data = f.read()

#data = example_data

data = [list(x) for x in data.splitlines()]
height = len(data)
width = len(data[0])
xmin = 0
xmax = width-1
ymin = 0
ymax = height-1

def printState(state):
    for row in state:
        print("".join(row))
    print("")

def isOccupied(state, x, y):
    if x < xmin or x > xmax or y < ymin or y > ymax:
        return False
    return state[y][x] == "#"

def countOccupiedNeighbours(state, cx, cy):
    total = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if x==0 and y == 0:
                continue
            if isOccupied(state,cx+x,cy+y):
                total += 1
    return total

def stepState(state):
    newstate = [["?" for col in row] for row in state]
    changes = 0

    for x in range(0,width):
        for y in range(0,height):
            if state[y][x] == ".":
                newstate[y][x] = "."
            elif state[y][x] == "L":
                newstate[y][x] = "L" if countOccupiedNeighbours(state,x,y) != 0 else "#"
            elif state[y][x] == "#": 
                newstate[y][x] = "L" if countOccupiedNeighbours(state,x,y) >= 4 else "#"
            changes += (0 if state[y][x] == newstate[y][x] else 1)

    return (changes,newstate)

def countTotalOccupied(state):
    total = 0
    for x in range(0,width):
        for y in range(0,height):
            if state[y][x] == "#": 
                total += 1
    return total

steps = 0
while True:
    (changes,data) = stepState(data)
    if changes == 0:
        break 
    steps += 1
print(steps)
print(countTotalOccupied(data))

