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

kFloor = 0
kEmpty = 1
kFull = 2
kChar = [".","L","#"]

def charToType(text):
    if text == ".":
        return kFloor
    elif text == "L":
        return kEmpty
    elif text == "#":
        return kFull
    else:
        raise NameError("Bad char")



class State:
    def __init__(self, input_string):
        self.seats = [[charToType(col) for col in row] for row in data.splitlines()]
        self.directiongrids = None
        self.leftseats = None
        self.height = len(self.seats)
        self.width = len(self.seats[0])
        self.last_changes = 0

    #part A update, just based off direct neighbours
    def update(self):
        new_seats = [[kFloor for col in row] for row in self.seats]
        changes = 0
        for x in range(0,self.width):
            for y in range(0,self.height):
                if self.seats[y][x] == kEmpty:
                    new_seats[y][x] = kEmpty if self.countOccupiedNeighbours(x,y) != 0 else kFull
                elif self.seats[y][x] == kFull: 
                    new_seats[y][x] = kEmpty if self.countOccupiedNeighbours(x,y) >= 4 else kFull
                if self.seats[y][x] != new_seats[y][x]:
                    changes += 1
        self.seats = new_seats
        self.last_changes = changes
        return changes

    #part B update, builds directional grids and uses to count directional neighbour types
    def update2(self):
        self.buildNeighbours()
        new_seats = [[kFloor for col in row] for row in self.seats]
        changes = 0
        for x in range(0,self.width):
            for y in range(0,self.height):
                if self.seats[y][x] == kFloor:
                    continue
                occupied = 0
                for grid in self.directiongrids:
                    if grid[y][x] == kFull:
                        occupied += 1
                if self.seats[y][x] == kEmpty:
                    new_seats[y][x] = kEmpty if occupied != 0 else kFull
                elif self.seats[y][x] == kFull: 
                    new_seats[y][x] = kEmpty if occupied >= 5 else kFull
                if self.seats[y][x] != new_seats[y][x]:
                    changes += 1
        self.seats = new_seats
        self.last_changes = changes
        return changes

    #for part A, just count total direct neighbours that are occupied
    def countOccupiedNeighbours(self, cx, cy):
        minx = max(cx-1,0)
        miny = max(cy-1,0)
        maxx = min(cx+2,self.width)
        maxy = min(cy+2,self.height)
        total = 0
        for y in range(miny,maxy):
            for x in range(minx,maxx):
                if x==cx and y==cy:
                    continue
                total += max(self.seats[y][x]-1,0) #1 if full seat, 0 otherwise
        return total
    
    #count total occupied seats in the grid
    def countTotalOccupied(self):
        total = 0
        for x in range(0,self.width):
            for y in range(0,self.height):
                if self.seats[y][x] == kFull: 
                    total += 1
        return total        

    #helper to print a grid
    def _printGrid(self, grid):
        for row in grid:
            print(" ".join([kChar[x] for x in row]))
        print("")

    #print the main state grid
    def printState(self):
        self._printGrid(self.seats)

    #sweeps from a given start position in a given direction to identify a set
    #of visible neighbours
    def _buildNeighboursFrom(self, start, direction, grid):
        pos = list(start)
        val = kFloor
        while pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height:
            seat = self.seats[pos[1]][pos[0]]
            if seat != kFloor:
                grid[pos[1]][pos[0]] = val 
                val = seat
            pos[0] += direction[0]
            pos[1] += direction[1]

    #for a given direction, calls _buildNeighboursFrom for all necessary starting
    #positions to fill the entire grid (note: for diagonals, counting centre line
    # twice but who gives a shit)
    def _buildDirectionNeighbours(self, direction):
        res = [[kFloor for col in row] for row in self.seats]

        if direction[0] != 0:
            xstart = 0 if direction[0] > 0 else self.width - 1 
            for y in range(0,self.height):
                self._buildNeighboursFrom((xstart,y), direction, res)

        if direction[1] != 0:
            ystart = 0 if direction[1] > 0 else self.height-1
            for x in range(0,self.width):
                self._buildNeighboursFrom((x,ystart), direction, res)

        #self._printGrid(res)
        return res
    
    #builds the directional grid for all 8 directions from every seat
    def buildNeighbours(self):
        self.directiongrids=[]
        for x in range(-1,2):
            for y in range(-1,2):
                if x != 0 or y != 0:
                    self.directiongrids.append(self._buildDirectionNeighbours((x,y)))



state = State(data)
steps = 0
while True:
    changes = state.update2()
    if changes == 0:
        break 
    steps += 1
print(steps)
print(state.countTotalOccupied())
