import re

example_data = """\
F10
N3
F7
R90
F11"""

with open("day12input.txt") as f:
    data = f.read()

#data = example_data

data = [ (x.group(1),int(x.group(2))) for x in [re.match(r"(\w)(\d+)",line) for line in data.splitlines()] ]

ship_pos = None
ship_vel = None

def runPartA():
    global ship_pos
    global ship_vel
    ship_pos = [0,0]
    ship_vel = [1,0]
    for command in data:
        op = command[0]
        val = command[1]
        if op == 'F':
            ship_pos[0] += ship_vel[0] * val
            ship_pos[1] += ship_vel[1] * val
        elif op == 'N':
            ship_pos[1] += val
        elif op == 'S':
            ship_pos[1] -= val
        elif op == 'E':
            ship_pos[0] += val
        elif op == 'W':
            ship_pos[0] -= val
        elif op == 'R':
            while val > 0:
                ship_vel = [ship_vel[1],-ship_vel[0]]
                val -= 90 
        elif op == 'L':
            while val > 0:
                ship_vel = [-ship_vel[1],ship_vel[0]]
                val -= 90

def runPartB():
    global ship_pos
    global ship_vel
    ship_pos = [0,0]
    ship_vel = [10,1]
    for command in data:
        op = command[0]
        val = command[1]
        if op == 'F':
            ship_pos[0] += ship_vel[0] * val
            ship_pos[1] += ship_vel[1] * val
        elif op == 'N':
            ship_vel[1] += val
        elif op == 'S':
            ship_vel[1] -= val
        elif op == 'E':
            ship_vel[0] += val
        elif op == 'W':
            ship_vel[0] -= val
        elif op == 'R':
            while val > 0:
                ship_vel = [ship_vel[1],-ship_vel[0]]
                val -= 90 
        elif op == 'L':
            while val > 0:
                ship_vel = [-ship_vel[1],ship_vel[0]]
                val -= 90

runPartA()
print(abs(ship_pos[0])+abs(ship_pos[1]))

runPartB()
print(abs(ship_pos[0])+abs(ship_pos[1]))

