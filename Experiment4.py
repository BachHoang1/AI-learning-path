#Project Experiment 5
from agent import Agent
from PDWorld import World
from PDWorld import Node
from SelectMove import SelectMove
from Storing import updateMatrix
from Visualize import Visual
import pygame
import copy
import random

class E5:
# Create agent in starting location with no package
    agent = Agent(0, 4, False)

# Create two worlds for when agent has/has no package
    havePackageWorld = World()
    noPackageWorld = World()

# Used to visualize grids
    show = Visual()

# Parameters for Visualize
    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []


# Run 200 operations with PRANDOM with a = 0.3, g = 0.5
    for i in range(500):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)
        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

# Show grids for PRANDOM
    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

# Run 7800 operations of PEXPLOIT
# When the agent reaches a terminal state the 2nd time, swap pickup/drop off locations
    terminalCounter = 0
    for i in range(5500):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)
        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)

        if world.isCompleteDelevery():
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps
            resetNumber += 1
            # pickup/dropoff are reset like normal for the first terminal state
            if terminalCounter == 0:
                noPackageWorld.mapReset()
                havePackageWorld.mapReset()
                terminalCounter += 1

            elif terminalCounter == 1:
                    noPackageWorld.mapReset()
                    havePackageWorld.mapReset()
                    terminalCounter += 1
            # pickup/dropoff are swapped on the third terminal state
            elif terminalCounter == 2:
                # swap on each map
                noPackageWorld.mapReset()
                havePackageWorld.mapReset()
                terminalCounter += 1
            elif terminalCounter == 3:
                # swap on each map
                noPackageWorld.mapChange()
                havePackageWorld.mapChange()
                terminalCounter += 1
            elif terminalCounter == 4:
                # swap on each map
                noPackageWorld.mapChange()
                havePackageWorld.mapChange()
                terminalCounter += 1
            elif terminalCounter == 5:
                # swap on each map
                noPackageWorld.mapChange()
                havePackageWorld.mapChange()
                terminalCounter += 1

        if (i == 1499 or i == 3499 or i == 5499):
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
            print("terminalCounter: " + str(terminalCounter))

# Print data
    print("terminalCounter: " + str(terminalCounter))

# Show grids for PEXPOLIT
    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
    show.quit()
