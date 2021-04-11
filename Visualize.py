#this file is used to visualize the pd world
import pygame
from agent import Agent
from PDWorld import World
from PDWorld import Node

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTGREY = (100, 100, 100)
AGENTCOLORNOBLOCK = (20, 180, 200)
AGENTCOLOWITHBLOCK = (255, 110, 250)
PICKUP = (38, 78, 142)
DROPOFF= (241, 66, 244)

TILESIZE = 100

class Visual:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 650))
        pygame.display.set_caption("Running of Group 7 Computer")

#world 1 is world with no packagr, world 2 is with package
    def draw(self, world1, world2, agent, resetNumber, terminationSteps):
        self.screen.fill(BLACK)
        #finding values needs to create the gradient
        w1Maxq = self.findMax(world1)
        w1MinQGreatherThanZero =self.findMinGreaterThanZero(world1)
        w1Minq = self.findMin(world1)
        w1MaxqLessThanZero = self.findMaxLessThanZero(world1)

        w2Maxq = self.findMax(world2)
        w2MinQGreatherThanZero = self.findMinGreaterThanZero(world2)
        w2Minq = self.findMin(world2)
        w2MaxqLessThanZero = self.findMaxLessThanZero(world2)

        #draw all nodes on both map on a screen
        for x in range(11):
            if x != 5:
                for y in range(5):
                    if x < 5:
                        self.drawNode(x, y, world1.map[x][y], w1Maxq, w1MinQGreatherThanZero,  w1Minq, w1MaxqLessThanZero)
                    else:
                        self.drawNode(x, y, world2.map[x-6][y], w2Maxq, w2MinQGreatherThanZero, w2Minq, w2MaxqLessThanZero)
                        
        # Draw pickup/dropoff dynamically
        for x in range(11):
            if x != 5:
                for y in range(5):
                    Ax = x * 100
                    Ay = y * 100
                    if x<5:
                        if (world1.map[x][y].isPickUp):
                            pygame.draw.rect(self.screen, PICKUP, [Ax, Ay, 100, 100], 5)
                        if (world1.map[x][y].isDropOff):
                            pygame.draw.rect(self.screen, DROPOFF, [Ax, Ay, 100, 100], 5)
                    else:
                        if (world2.map[x-6][y].isPickUp):
                            pygame.draw.rect(self.screen, PICKUP, [Ax, Ay, 100, 100], 5)
                        if (world2.map[x-6][y].isDropOff):
                            pygame.draw.rect(self.screen, DROPOFF, [Ax, Ay, 100, 100], 5)


        #highlight pickup, dropoff, agent location, and some information about the state space
        self.drawAgentLocationLeftMap(agent)
        self.drawAgentLocationRightMap(agent)
        self.addText(agent, resetNumber, terminationSteps)
        pygame.display.flip()

# Adds text to label grids, and show counter/reward, number of reset
    def addText(self, agent, resetNumber, terminationSteps):
        font = pygame.font.SysFont('Arial', 30)
        info = "Agent without package"
        text = font.render(info, False, WHITE)
        self.screen.blit(text, (0, 500))

        info2 = "Agent with package"
        text = font.render(info2, False, WHITE)
        self.screen.blit(text, (600, 500))

        info3 = "Operator Counter: " + str(agent.steps)
        text = font.render(info3, False, WHITE)
        self.screen.blit(text, (0, 550))

        info4 = "Agent Reward: " + str(agent.score)
        text = font.render(info4, False, WHITE)
        self.screen.blit(text, (400, 550))

        info5 = "Map Reset Counter: " + str(resetNumber)
        text = font.render(info5, False, WHITE)
        self.screen.blit(text, (800, 550))

        if len(terminationSteps) >= 10:
            font = pygame.font.SysFont('Arial', 27)
        info3 = "Steps taken to reach terminal state: " + ', '.join(map(str, terminationSteps))
        text = font.render(info3, False, WHITE)
        self.screen.blit(text, (0, 600))

# Function to determine color gradient based on max and min q values
    def getGradient(self, maxq, minQGreaterThanZero,  minq, maxQSmallerThanZero, currq):
        g = 0
        r = 0
        #error prevention features
        smaxq = maxq
        sminq = minq
        if maxq == 0:
            smaxq = 1
        if minq == 0:
            sminq = 1
        if currq > maxq or currq < minq:
            return (0,0,255)

        if currq == 0:
            return LIGHTGREY
        elif currq > 0:
            scale = (currq) / (smaxq)
            g = scale*255
        else:
            #a different equation is used to create bigger difference between
            #a linear function is chosen for avoiding no distortion in relations to the path that need to avoid
            scale = (currq - maxQSmallerThanZero)/ (sminq - maxQSmallerThanZero)
            r = scale*255
        return (r,g,0)

# Keeps window open until we quit by closing window
# Set self.playing = False to end the game
    def run_visual(self, world1, world2, agent, resetNumber, terminationSteps):
        self.running = True
        while self.running:
            pygame.time.delay(1000)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
            self.draw(world1, world2, agent, resetNumber, terminationSteps)

    def quit(self):
        pygame.quit()


#fill in each squares with 4 triangle, with the q-value
    def drawNode(self, x, y, node, maxq, minQGreaterThanZero,  minq, maxQSmallerThanZero):
        x *= 100
        y *= 100
        text = pygame.font.SysFont('Arial', 16)

        #north
        color = self.getGradient(maxq, minQGreaterThanZero,  minq, maxQSmallerThanZero, node.qNorth)
        pygame.draw.polygon(self.screen, color, [(x, y), (x + TILESIZE, y), ( x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x + TILESIZE, y), ( x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qNorth, 2)), False, WHITE)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 10)))

        #east
        color = self.getGradient(maxq, minQGreaterThanZero,  minq, maxQSmallerThanZero, node.qEast)
        pygame.draw.polygon(self.screen, color, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qEast, 2)), False, WHITE)
        self.screen.blit(textCanvas, (x + ((3 * TILESIZE) / 4) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 2) - (textCanvas.get_rect().height / 2)))

        #south
        color = self.getGradient(maxq, minQGreaterThanZero,  minq, maxQSmallerThanZero, node.qSouth)
        pygame.draw.polygon(self.screen, color, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qSouth, 2)), False, WHITE)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + 75 - (textCanvas.get_rect().height / 2)))

        #west
        color = self.getGradient(maxq, minQGreaterThanZero,  minq, maxQSmallerThanZero, node.qWest)
        pygame.draw.polygon(self.screen, color, [(x, y), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qWest, 2)), False, WHITE)
        self.screen.blit(textCanvas, (x + (TILESIZE / 4) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 2) - (textCanvas.get_rect().height / 2)))

        if (node.isPickUp or node.isDropOff):
            pygame.draw.polygon(self.screen, BLACK, [(x, y), (x + 20, y), (x + 20, y + 20), (x, y + 20)])
            textCanvas = text.render(str(node.blockCount), False, WHITE)
            self.screen.blit(textCanvas, (x + 10 - (textCanvas.get_rect().width / 4), y + 7 - (textCanvas.get_rect().height / 4)))


    def drawAgentLocationLeftMap(self, agent):
        xPosition =  int((agent.x * TILESIZE) + (TILESIZE / 2))
        yPosition =  int((agent.y * TILESIZE) + (TILESIZE / 2))
        if not (agent.havePackage):
            AGENTCOLOR = AGENTCOLORNOBLOCK
        else:
            AGENTCOLOR = AGENTCOLOWITHBLOCK
        pygame.draw.circle(self.screen, AGENTCOLOR, (xPosition , yPosition), 10)

    def drawAgentLocationRightMap(self, agent):
        xPosition =  int((agent.x * TILESIZE) + (TILESIZE / 2))
        yPosition =  int((agent.y * TILESIZE) + (TILESIZE / 2))
        if not (agent.havePackage):
            AGENTCOLOR = AGENTCOLORNOBLOCK
        else:
            AGENTCOLOR = AGENTCOLOWITHBLOCK
        pygame.draw.circle(self.screen, AGENTCOLOR, (xPosition + 6 * TILESIZE, yPosition), 10)


# This function finds the max or min given a world, oldX and oldY. Returns highest or lowest q
    def findMax(self, world):
        #pick a random baseline from the list
        max = world.map[0][0].qNorth
        for i in range(5):
            for j in range(5):
                if (world.map[i][j].qNorth) > max:
                    max = world.map[i][j].qNorth
                if (world.map[i][j].qEast) > max:
                    max = world.map[i][j].qEast
                if (world.map[i][j].qSouth) > max:
                    max = world.map[i][j].qSouth
                if (world.map[i][j].qWest) > max:
                    max = world.map[i][j].qWest
        return max

    def findMin(self, world):
        min = world.map[0][0].qNorth
        for i in range(5):
            for j in range(5):
                if (world.map[i][j].qNorth) < min:
                    min = world.map[i][j].qNorth
                if (world.map[i][j].qEast) < min:
                    min = world.map[i][j].qEast
                if (world.map[i][j].qSouth) < min:
                    min = world.map[i][j].qSouth
                if (world.map[i][j].qWest) < min:
                    min = world.map[i][j].qWest
        return min
# following 2 function are used to improve the gradient of the color
    def findMinGreaterThanZero(self, world):
        min = self.findMax(world)
        for i in range(5):
            for j in range(5):
                if (world.map[i][j].qNorth < min and world.map[i][j].qNorth > 0):
                    min = world.map[i][j].qNorth
                if (world.map[i][j].qEast < min and world.map[i][j].qEast > 0):
                    min = world.map[i][j].qEast
                if (world.map[i][j].qSouth < min and world.map[i][j].qSouth > 0):
                    min = world.map[i][j].qSouth
                if (world.map[i][j].qWest < min and world.map[i][j].qWest > 0):
                    min = world.map[i][j].qWest
        return min

    def findMaxLessThanZero(self, world):
        max = self.findMin(world)
        for i in range(5):
            for j in range(5):
                if (world.map[i][j].qNorth > max and world.map[i][j].qNorth < 0):
                    max = world.map[i][j].qNorth
                if (world.map[i][j].qEast > max and world.map[i][j].qEast < 0):
                    max = world.map[i][j].qEast
                if (world.map[i][j].qSouth > max and world.map[i][j].qSouth < 0):
                    max = world.map[i][j].qSouth
                if (world.map[i][j].qWest > max and world.map[i][j].qWest < 0):
                    max = world.map[i][j].qWest
        return max
