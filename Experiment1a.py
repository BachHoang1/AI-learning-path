# Project Experiment 1a
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
import pygame
from Visualize import Visual


class E1a:
    agent = Agent(0, 4, False)
    havePackageWorld = World()
    noPackageWorld = World()

    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []

    show = Visual()

    for i in range(500):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
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

    # Show progress after PRANDOM
    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    # Show progress at fixed intervals
    for i in range(5500):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if (i == 1499 or i == 3499 or i == 5499):
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
    show.quit()
