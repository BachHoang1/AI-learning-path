#QMatrix/SARSA updates and storing written by Logan F.
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove


class updateMatrix:

#this method find out what opeorator is applied given old and new agents
    def moveDirection(oldAgent, newAgent) -> int:
        # 0,1,2,3,4 for North, East, South, West, stayput(pickup/dropoff)
        # if stayput
        if (newAgent.x == oldAgent.x and newAgent.y == oldAgent.y):
            return 4
        # moved north
        elif (newAgent.y < oldAgent.y and newAgent.x == oldAgent.x):
            return 0
        # moved East
        elif (newAgent.x > oldAgent.x and newAgent.y == oldAgent.y):
            return 1
        # moved south
        elif (newAgent.y > oldAgent.y and newAgent.x == oldAgent.x):
            return 2
        # moved West
        elif (newAgent.x < oldAgent.x and newAgent.y == oldAgent.y):
            return 3


    #Updating using Q-Learing
    def QUpdate(agentOld, agentCurr, world, alpha, gamma):
        reward = agentCurr.score - agentOld.score

        oldX = agentOld.x
        oldY = agentOld.y
        newX = agentCurr.x
        newY = agentCurr.y

        applicable = []

        if(agentCurr.canMoveNorth()):
            applicable.append(world.map[newX][newY].qNorth)
        if (agentCurr.canMoveEast()):
            applicable.append(world.map[newX][newY].qEast)
        if (agentCurr.canMoveSouth()):
            applicable.append(world.map[newX][newY].qSouth)
        if (agentCurr.canMoveWest()):
            applicable.append(world.map[newX][newY].qWest)


        #nextBestQ = max(world.map[newX][newY].qNorth, world.map[newX][newY].qEast, world.map[newX][newY].qSouth, world.map[newX][newY].qEast)
        nextBestQ = max(applicable)

        movement = updateMatrix.moveDirection(agentOld, agentCurr)
        if(movement == 0):
            #We have moved north
            world.map[oldX][oldY].qNorth = ((1-alpha)*(world.map[oldX][oldY].qNorth)) + ((alpha)*(reward + ((gamma)*nextBestQ)))
        elif(movement == 1):
            # We have moved east
            world.map[oldX][oldY].qEast = ((1-alpha)*(world.map[oldX][oldY].qEast)) + ((alpha)*(reward + ((gamma)*nextBestQ)))
        elif (movement == 2):
            # We have moved east
            world.map[oldX][oldY].qSouth = ((1-alpha)*(world.map[oldX][oldY].qSouth)) + ((alpha)*(reward + ((gamma)*nextBestQ)))
        elif (movement == 3):
            # We have moved east
            world.map[oldX][oldY].qWest = ((1-alpha)*(world.map[oldX][oldY].qWest)) + ((alpha)*(reward + ((gamma)*nextBestQ)))
        elif (movement == 4):
            #update all direction as 1 state
            if(agentOld.canMoveNorth()):
                world.map[oldX][oldY].qNorth = ((1-alpha)*(world.map[oldX][oldY].qNorth)) + ((alpha)*(reward + ((gamma)*nextBestQ)))
            if (agentOld.canMoveEast()):
                world.map[oldX][oldY].qEast = ((1-alpha)*(world.map[oldX][oldY].qEast)) + ((alpha)*(reward + ((gamma)*nextBestQ)))
            if (agentOld.canMoveSouth()):
                world.map[oldX][oldY].qSouth = ((1-alpha)*(world.map[oldX][oldY].qSouth)) + ((alpha)*(reward + ((gamma)*nextBestQ)))
            if (agentOld.canMoveWest()):
                world.map[oldX][oldY].qWest = ((1-alpha)*(world.map[oldX][oldY].qWest)) + ((alpha)*(reward + ((gamma)*nextBestQ)))

    #this method will update the q vlaue 2 moves ago, as 2 moves are needed to SARSA to have all information
    def SARSAUpdate(agent1, agent2, agent3, world, alpha, gamma):
        #agent 1,2,3 is 2 moves ago, 1 moves ago, and current agnet
        move1 = updateMatrix.moveDirection(agent1, agent2);
        move2 = updateMatrix.moveDirection(agent2, agent3);
        #move 1 is opeorator applied on state 1 to get to state 2, and move 2 is from 2 to 3

        state2Q = [world.map[agent2.x][agent2.y].qNorth, world.map[agent2.x][agent2.y].qEast, world.map[agent2.x][agent2.y].qSouth, world.map[agent2.x][agent2.y].qWest]

        #if agent stays on the same state, like 2 -> pickup -> 2, then we will piack the best q on state 2 to update
        if(move2 == 4):
            move2 = state2Q.index(max(state2Q))


        reward = agent2.score - agent1.score
        if (move1 == 0):
            # We have moved north
            world.map[agent1.x][agent1.y].qNorth = ((1 - alpha) * (world.map[agent1.x][agent1.y].qNorth)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
        elif (move1 == 1):
            # We have moved east
            world.map[agent1.x][agent1.y].qEast = ((1 - alpha) * (world.map[agent1.x][agent1.y].qEast)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
        elif (move1 == 2):
            # We have moved south
            world.map[agent1.x][agent1.y].qSouth = ((1 - alpha) * (world.map[agent1.x][agent1.y].qSouth)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
        elif (move1 == 3):
            # We have moved west
            world.map[agent1.x][agent1.y].qWest = ((1 - alpha) * (world.map[agent1.x][agent1.y].qWest)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
        elif (move1 == 4):
            # update all direction as 1 state
            if (agent1.canMoveNorth()):
                world.map[agent1.x][agent1.y].qNorth = ((1 - alpha) * (world.map[agent1.x][agent1.y].qNorth)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
            if (agent1.canMoveEast()):
                world.map[agent1.x][agent1.y].qEast = ((1 - alpha) * (world.map[agent1.x][agent1.y].qEast)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
            if (agent1.canMoveSouth()):
                world.map[agent1.x][agent1.y].qSouth = ((1 - alpha) * (world.map[agent1.x][agent1.y].qSouth)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
            if (agent1.canMoveWest()):
                world.map[agent1.x][agent1.y].qWest = ((1 - alpha) * (world.map[agent1.x][agent1.y].qWest)) + ((alpha) * (reward + (gamma) * state2Q[move2]))
        #we will put all 4  value of state 2 into








