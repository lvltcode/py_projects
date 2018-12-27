#!/usr/bin/env python
import sys
import math
import random

def getBoard():
  sys.stdin.readline()
  board = []
  while True:
      x = sys.stdin.readline()
      if x[0] != "#":
          break
      board.append(x.rstrip('\n'))
  return board

def getPos(board):
  for i in range(len(board)):
      for j in range(len(board[i])):
          if board[i][j] == "#":
              w.append([j,i])
          if board[i][j] == "o":
              o.append([j,i])
          if board[i][j] == "!":
              bon.append([j,i])
          if board[i][j] == 'A':
              A.append(j)
              A.append(i)

def findMinDistance(listpoint, cur):
  minpoint = listpoint[0]
  for i in listpoint:
      d1= math.sqrt(abs(i[0]-cur[0])**2 + abs(i[1]-cur[1])**2)
      d2= math.sqrt(abs(minpoint[0]-cur[0])**2 + abs(minpoint[1]-cur[1])**2)
      if d1 <= d2:
          minpoint = i
  return minpoint


def validMove(cur, wall):
  pos = [[0,1],[0,-1],[1,0],[-1,0]]
  valid = ["MOVE UP", "MOVE DOWN", "MOVE RIGHT", "MOVE LEFT"]
  for i in pos:
      temp = [0,0]
      temp[0] = cur[0] + i[0]
      temp[1] = cur[1] + i[1]
      if temp in wall:
          if i == [0,1]:
              valid.remove("MOVE DOWN")
          if i == [0,-1]:
              valid.remove("MOVE UP")
          if i == [1,0]:
              valid.remove("MOVE RIGHT")
          if i == [-1,0]:
              valid.remove("MOVE LEFT")
  return valid

# def move(cur, point, valid):
#     temp = valid
#     if point[0] < cur[0] and "MOVE LEFT" in valid:
#         return "MOVE LEFT\n"
#     if point[0] > cur[0] and "MOVE RIGHT" in valid:
#         return "MOVE RIGHT\n"
#     if point[1] < cur[1] and "MOVE UP" in valid:
#         return "MOVE UP\n"
#     if point[1] > cur[1] and "MOVE DOWN" in valid:
#         return "MOVE DOWN\n"
#     else:
#         if len(valid) == 1:
#             return temp[0] + '\n'
#         else:
#             return temp[random.randint(0, len(valid) - 1)] + '\n'

def move(cur, point, valid):
  temp = valid
  if point[0] < cur[0] and "MOVE LEFT" in valid:
      return "MOVE LEFT\n"
  if point[0] > cur[0] and "MOVE RIGHT" in valid:
      return "MOVE RIGHT\n"
  if point[1] < cur[1] and "MOVE UP" in valid:
      return "MOVE UP\n"
  if point[1] > cur[1] and "MOVE DOWN" in valid:
      return "MOVE DOWN\n"
  else:
      if len(valid) == 1:
          return temp[0] + '\n'
      else:
          return temp[random.randint(0, len(valid) - 1)] + '\n'



sys.stdin.readline()
sys.stdin.readline()
sys.stdout.write('I AM A\n\n')
sys.stdin.readline()
sys.stdin.readline()
sys.stdout.write('OK\n\n')

way = {}
while True:
  w = []
  o = []
  A = []
  bon = []


  y = getBoard()
  getPos(y)
  valid = validMove(A,w)

  item = (A[0],A[1])
  if item not in way.keys():
      way[item] = 0
  else:
      way[item] = way[item] + 1


  f = open("abc","a")
  f.write(str(way)+'\n')
  f.close()

  if len(bon) != 0:
      print(move(A, findMinDistance(bon, A), valid))
  else:
      print(move(A, findMinDistance(o, A), valid))
