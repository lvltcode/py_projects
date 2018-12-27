#!/usr/bin/env python3
import sys
import math
import random
import string


# function that help to prinze the maze/square
def printMaze():
    maze = []
    lineOfMaze = sys.stdin.readline()
    while lineOfMaze[0] == '#':
        maze.append(lineOfMaze.rstrip('\n'))
        lineOfMaze = sys.stdin.readline()
    protocole = open('protocol', 'w')
    for lines in maze:
        protocole.write(str(lines) + '\n')
    protocole.close()
    return maze


# find the agents and the treasure's positions
def positionAgent(maze):
    position = []
    row = len(maze)
    col = len(maze[0])
    for x in range(1, row):
        for y in range(1, col):
            if maze[x][y] in string.ascii_uppercase:
                position.append([x, y])
                sys.stderr.write(str(position) + "\n\n")
    return position


# for finding the way to earn treasues
# generate number from 2 position of agent and treasures
# then find way to move
def tre(maze, position):
    treasures = []
    row = len(maze)
    col = len(maze[0])
    for x in range(1, row-1):
        for y in range(1, col-1):
            if maze[x][y] == '!':
                treasures.insert(0, [x, y])
            elif maze[x][y] == 'o':
                treasures.append([x, y])
    sys.stderr.write(str(treasures) + "\n\n")
    return treasures


def near(maze, position, treasures):
    nearest = []
    min = abs(position[0][0]-treasures[0][0]) + abs(
            (position[0][1] - treasures[0][1]))
    point = treasures[0]
    for i in range(len(treasures)):
        if min > abs(position[0][0]-treasures[i][0]) + abs(
                position[0][1] - treasures[i][1]):
            min = abs(position[0][0]-treasures[i][0]) + abs(
                position[0][1] - treasures[i][1])
            point = treasures[i]
    nearest.append(point)
    sys.stderr.write(str(nearest) + "\n\n")
    return nearest


def pathFinding(maze, position, nearest):
    if position[0][1] - nearest[0][1] > 0:
        sys.stdout.write('MOVE LEFT\n\n')
    elif position[0][1] - nearest[0][1] < 0:
        sys.stdout.write('MOVE RIGHT\n\n')
    else:
        if position[0][0] - nearest[0][0] > 0:
            sys.stdout.write('MOVE UP\n\n')
        elif position[0][0] - nearest[0][0] < 0:
            sys.stdout.write('MOVE DOWN\n\n')


# main
virtualMessage = sys.stdin.readline()
while virtualMessage != '':
    if 'HELLO' in virtualMessage:
        sys.stdout.write('I AM A\n\n')
    if 'YOU ARE A' in virtualMessage:
        sys.stdout.write('OK\n\n')
    if 'MAZE' in virtualMessage:
        maze = printMaze()
        position = positionAgent(maze)
        treasures = tre(maze, position)
        nearest = near(maze, position, treasures)
        path = pathFinding(maze, position, nearest)
    virtualMessage = sys.stdin.readline()
