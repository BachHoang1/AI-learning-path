#Project Experiment 2
from agent import Agent
from PDWorld import World
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
from Visualize import Visual


# Using the SARSA algorithm
class E32:
    agent = Agent(0, 4, False)
    havePackageWorld = World()
    noPackageWorld = World()

    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []

    show = Visual()

    fiveBlock = True

    for i in range(500):
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
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.45, 0.5)
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
    for i in range(5500):
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
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.45, 0.5)
        if (i == 1499 or i == 3499 or i == 5499):
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

