#this file contains all seelct move algorithem, PRANDOM, PEPLOID, PGREEDY
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random


class SelectMove:
#path finding
#roll untill a random valid move 0,1,2,3 corrispond to north, east, south, west

#select at complete random
    def PRANDOM(agent, world, printMove):
        if(SelectMove.canPickUpAndDropOff(agent, world)):
            SelectMove.pickUpAndDropOff(agent, world, printMove)
        else:
            legalMove = False
            while not (legalMove):
                move = random.randint(0,3)
                if(move == 0 and agent.canMoveNorth()):
                    agent.moveNorth()
                    legalMove = True
                    if(printMove):
                        print("Agent moved North")
                elif(move == 1 and agent.canMoveEast()):
                    agent.moveEast()
                    legalMove = True
                    if (printMove):
                        print("Agent moved East")
                elif (move == 2 and agent.canMoveSouth()):
                    agent.moveSouth()
                    legalMove = True
                    if (printMove):
                        print("Agent moved South")
                elif (move == 3 and agent.canMoveWest()):
                    agent.moveWest()
                    legalMove = True
                    if (printMove):
                        print("Agent moved West")

#select best move at 80%, random at 20%
    def PEPLOIT(agent, world, printMove):
        if (SelectMove.canPickUpAndDropOff(agent, world)):
            SelectMove.pickUpAndDropOff(agent, world, printMove)
        else:
            rand = random.randint(1,10)
            #at 20% change, select randomly
            if(rand <= 2):
                SelectMove.PRANDOM(agent, world, printMove)
            #at 80% select the best q value
            elif(rand > 2 and rand <= 10):
                move = SelectMove.findBestQValue(agent, world.map[agent.x][agent.y])
                if (move == 0 and agent.canMoveNorth()):
                    agent.moveNorth()
                    legalMove = True
                    if (printMove):
                        print("Agent moved North")
                elif (move == 1 and agent.canMoveEast()):
                    agent.moveEast()
                    legalMove = True
                    if (printMove):
                        print("Agent moved East")
                elif (move == 2 and agent.canMoveSouth()):
                    agent.moveSouth()
                    legalMove = True
                    if (printMove):
                        print("Agent moved South")
                elif (move == 3 and agent.canMoveWest()):
                    agent.moveWest()
                    legalMove = True
                    if (printMove):
                        print("Agent moved West")


#select move with best q-value
    def PGREEDY(agent, world, printMove):
        if (SelectMove.canPickUpAndDropOff(agent, world)):
            SelectMove.pickUpAndDropOff(agent, world, printMove)
        else:
            move = SelectMove.findBestQValue(agent, world.map[agent.x][agent.y])
            if (move == 0 and agent.canMoveNorth()):
                agent.moveNorth()
                legalMove = True
                if (printMove):
                    print("Agent moved North")
            elif (move == 1 and agent.canMoveEast()):
                agent.moveEast()
                legalMove = True
                if (printMove):
                    print("Agent moved East")
            elif (move == 2 and agent.canMoveSouth()):
                agent.moveSouth()
                legalMove = True
                if (printMove):
                    print("Agent moved South")
            elif (move == 3 and agent.canMoveWest()):
                agent.moveWest()
                legalMove = True
                if (printMove):
                    print("Agent moved West")

#this method select the move with best q value, break tie by rolling a dice
#0,1,2,3 for North, East, South, West
    def findBestQValue(agent, node) -> int:

        value = []
        # append all legal move
        if (agent.canMoveNorth()):
            value.append(node.qNorth)
        if (agent.canMoveEast()):
            value.append(node.qEast)
        if (agent.canMoveSouth()):
            value.append(node.qSouth)
        if (agent.canMoveWest()):
            value.append(node.qWest)

        value.sort(reverse=True)
        #if frist 2 value is not the same, there is no tie
        if not (value[0] == value[1]):
            if(node.qNorth == value[0] and agent.canMoveNorth()):
                return 0
            elif(node.qEast == value[0] and agent.canMoveEast()):
                return 1
            elif(node.qSouth == value[0] and agent.canMoveSouth()):
                return 2
            elif(node.qWest == value[0] and agent.canMoveWest()):
                return 3
            # append all highest index into a list, and draw a random one
        else:
            #select all that == to largest and roll the die
            list = []
            if (node.qNorth == value[0] and agent.canMoveNorth()):
                list.append(0)
            if (node.qEast == value[0] and agent.canMoveEast()):
                list.append(1)
            if (node.qSouth == value[0] and agent.canMoveSouth()):
                list.append(2)
            if (node.qWest == value[0] and agent.canMoveWest()):
                list.append(3)
            return list[random.randint(0, (len(list) - 1))]

#this method will pickup/dropoff if applicable
    def pickUpAndDropOff(agent, world, printMove):
        if (world.map[agent.x][agent.y].isPickUp and world.map[agent.x][agent.y].canPickUpBlock() and agent.canPickUp()):
            world.map[agent.x][agent.y].pickUpAblock()
            agent.pickUpPackage()
            if (printMove):
                print("Agent Picked Up Block")
        elif (world.map[agent.x][agent.y].isDropOff and world.map[agent.x][agent.y].canDropOffBlock() and agent.canDropOff()):
            world.map[agent.x][agent.y].dropOffBlock()
            agent.dropOffPackage()
            if (printMove):
                print("Agent Dropped Off Block")


#this method checks if pickup/dropoff is applicable
    def canPickUpAndDropOff(agent, world) -> bool:
        return ((world.map[agent.x][agent.y].isPickUp and world.map[agent.x][agent.y].canPickUpBlock() and agent.canPickUp()) or
                (world.map[agent.x][agent.y].isDropOff and world.map[agent.x][agent.y].canDropOffBlock() and agent.canDropOff()))

