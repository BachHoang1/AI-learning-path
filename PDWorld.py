#this PDworld contatins the world as 2, 2d arrays, for agent carrrying and not carrying a block

class Node:
    #x, y is position, isPickUp/DropOff refer to is a pick or drop off location, block count is how many block is in the node
    #update them if they are assigned to be a pick up or drop off
    def __init__(self):
        self.isPickUp = False
        self.isDropOff = False
        self.blockCount = 0
        self.qNorth = 0
        self.qEast = 0
        self.qSouth = 0
        self.qWest = 0

#a set of function that checks and apply opeorator to the world
    def pickUpAblock(self):
        if(self.isPickUp and self.blockCount > 0):
                self.blockCount -= 1

    def canPickUpBlock(self) -> bool:
        if (self.isPickUp and self.blockCount > 0):
            return True
        else:
            return False


    def dropOffBlock(self):
        if(self.isDropOff and self.blockCount < 5):
            self.blockCount += 1

    def canDropOffBlock(self) -> bool:
        if(self.isDropOff and self.blockCount < 5):
            return True
        else:
            return False

class World:
    # this initialize the map for the class

    #this method the world, with pickup and drop off location set
    def __init__(self):
        cols = 5
        rows = 5
        self.map = [[Node() for j in range(cols)] for i in range(rows)]

        self.setPickUp(1, 3)
        self.setPickUp(4, 2)


        self.setDropOff(0, 0)
        self.setDropOff(4, 0)
        self.setDropOff(2, 2)
        self.setDropOff(4, 4)


    #set block as pickUpBlock
    def setPickUp(self, x, y):
        self.map[x][y].isPickUp = True
        self.map[x][y].blockCount = 5
    #set block as dropOffBlock
    def setDropOff(self, x, y):
        self.map[x][y].isDropOff = True

    def printWorld(self):
        for x in range(0, 5):
            for y in range(0, 5):
                print("Location: " + str(x) + " " + str(y))
                print("North: " + str(self.map[x][y].qNorth) + " " + "East: " + str(self.map[x][y].qEast) + " " + "South: " + str(self.map[x][y].qSouth) + " " + "West: " + str(self.map[x][y].qWest))

    #this mothod checks if all pickup have package in rither pickup or dropoff
    def isCompleteDelevery(self) -> bool:
        for x in range(0, 5):
            for y in range(0, 5):
                if(self.map[x][y].isPickUp and self.map[x][y].blockCount > 0):
                    return False

        #if all pickup have 0 block or all dropoff have 5, return True
        return True

    #this moethod invert pick up and drop off on a map.
    def invertPickUpDropOff(self):
        for x in range(0, 5):
            for y in range(0, 5):
                if(self.map[x][y].isPickUp):
                    self.map[x][y].isPickUp = False
                    self.map[x][y].isDropOff = True
                    self.map[x][y].blockCount = 0

                elif(self.map[x][y].isDropOff):
                    self.map[x][y].isDropOff = False
                    self.map[x][y].isPickUp = True
                    self.map[x][y].blockCount = 5

    #map reset on
    def mapReset(self):
        for x in range(0, 5):
            for y in range(0, 5):
                if (self.map[x][y].isPickUp):
                    self.map[x][y].blockCount = 5
                elif (self.map[x][y].isDropOff):
                    self.map[x][y].blockCount = 0

    def mapChange(self):
        self.setPickUp(3, 1)
        self.map[1][3].isPickUp = False

    #update world2's blockcount on all nodes to world1
    def worldUpdate(self, world1, world2):
        for x in range(0, 5):
            for y in range(0, 5):
                world2.map[x][y].blockCount = world1.map[x][y].blockCount
