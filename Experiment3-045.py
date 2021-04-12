#Project Experiment 2
from agent import Agent
from PDWorld import World
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
from Visualize import Visual


# Using the SARSA algorithm
class E2:
    show = Visual()

    agent = Agent(0, 4, False)
    oldAgent1 = copy.deepcopy(agent)

    havePackageWorld = World()
    noPackageWorld = World()

    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []

    # Run 500 steps with policy PRANDOM,
    for i in range(500):
        oldAgent2 = copy.deepcopy(oldAgent1)
        oldAgent1 = copy.deepcopy(agent)

        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)

        if i >= 1:
            if not oldAgent2.havePackage:
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, noPackageWorld, .45, .5)
            elif oldAgent2.havePackage:
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, havePackageWorld, .45, .5)

        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("map has been reset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    # Run 5500 steps with policy PEXPLOIT
    for j in range(5500):
        oldAgent2 = copy.deepcopy(oldAgent1)
        oldAgent1 = copy.deepcopy(agent)

        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)

        if j >= 1:
            if not oldAgent2.havePackage:
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, noPackageWorld, .45, .5)
            elif oldAgent2.havePackage:
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, havePackageWorld, .45, .5)

        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("map has been reset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

        if j == 1499 or j == 3499 or j == 5499:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    show.quit()
