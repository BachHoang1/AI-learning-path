# Project Experiment 2
# modified to produce picture needed for experiment2
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
import pygame
from Visualize import Visual


class E2:
    agent = Agent(0, 4, False)
    havePackageWorld = World()
    noPackageWorld = World()

    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []

    show = Visual()

    fiveBlock = True

    for i in range(200):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        if(fiveBlock):
            for x in range (0,5):
                for y in range(0,5):
                    if(world.map[x][y].blockCount == 5 and world.map[x][y].isDropOff):
                        show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
                        fiveBlock = False

        SelectMove.PRANDOM(agent, world, False)

        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if world.isCompleteDelevery():
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

    # Show progress after PRANDOM
    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    # Show progress at fixed intervals
    for i in range(7800):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        if(fiveBlock):
            for x in range (0,5):
                for y in range(0,5):
                    if(world.map[x][y].blockCount == 5 and world.map[x][y].isDropOff):
                        show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
                        fiveBlock = False

        SelectMove.PEPLOIT(agent, world, False)

        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if (i == 1799 or i == 3799 or i == 5799 or i == 7799):
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

        if world.isCompleteDelevery():
            world.worldUpdate(world, noPackageWorld)
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
    show.quit()

# sample for how to apply opeoratoes
#update score after every move

#SelectMove.PEPLOIT(agent, world, printMove= False)

#SelectMove.PRANDOM(agent, world, printMove= False)

#SelectMove.PGREEDY(agent, world, printMove= False)