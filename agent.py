#this class catains the information about the agent
class Agent:
    def __init__(self, startingX, startingY, havePackage):
        self.x = startingX
        self.y = startingY
        self.havePackage = havePackage
        self.score = 0
        self.steps = 0

#map is inverted, 0 at top, 4 at botton
    #set of move opeorator
    def moveNorth(self):
        if(self.y - 1 >= 0):
            self.y -= 1
            self.score -= 1
            self.steps += 1
        else:
            print("(up) is not a valid move")

    def moveSouth(self):
        if(self.y + 1 <= 4):
            self.y += 1
            self.score -= 1
            self.steps += 1
        else:
            print("(down) is not a valid move")

    def moveWest(self):
        if(self.x - 1 >= 0):
            self.x -= 1
            self.score -= 1
            self.steps += 1
        else:
            print("(left) is not a valid move")

    def moveEast(self):
        if(self.x + 1 <= 4):
            self.x += 1
            self.score -= 1
            self.steps += 1
        else:
            print("(right) is not a valid move")

    def pickUpPackage(self):
        if not (self.havePackage):
            self.havePackage = True
            self.score += 13
            self.steps += 1
        else:
            print("(pick up package) is not a valid move")

    def dropOffPackage(self):
        if(self.havePackage):
            self.havePackage = False
            self.score += 13
            self.steps += 1
        else:
            print("(drop off package) is not a valid move")

    #set of check can apply opeorator
    def canMoveNorth(self) -> bool:
        if(self.y - 1 >= 0):
            return True
        else:
            return False

    def canMoveSouth(self) -> bool:
        if(self.y + 1 <= 4):
            return True
        else:
            return False

    def canMoveWest(self):
        if(self.x - 1 >= 0):
            return True
        else:
            return False

    def canMoveEast(self):
        if(self.x + 1 <= 4):
            return True
        else:
            return False

    def canPickUp(self):
        return not (self.havePackage)

    def canDropOff(self):
        return self.havePackage