from collections import defaultdict
from math import floor

def solve(input_str: str):
  result = 0

  l = []

  w = 101
  h = 103
  # w = 11
  # h = 7


  grid = defaultdict(list)

  for line in input_str.split('\n'):
    line = line.replace('p=','').replace('v=','').split()
    pos = line[0].split(',')
    v = line[1].split(',')
    grid[(int(pos[0]), int(pos[1]))].append((int(v[0]), int(v[1])))


  for i in range(100):
    new_grid = defaultdict(list)
    for key, v in grid.items():
      while len(v):
        robot = v.pop()
        x = (key[0] + robot[0]) % w
        y = (key[1] + robot[1]) % h
        new_grid[(abs(x), abs(y))].append(robot)

    grid = new_grid


  qx = floor((w-1)/2)
  qy = floor((h-1)/2)

  q1 = 0
  for x in range(qx):
    for y in range(qy):
      print(x,y)
      q1 += len(grid[(x,y)])

  q2 = 0
  for x in range(w, qx, -1):
    for y in range(qy):
      print(x,y)
      q2 += len(grid[(x,y)])

  q3 = 0
  for x in range(qx):
    for y in range(h, qy, -1):
      print(x,y)
      q3 += len(grid[(x,y)])

  q4 = 0
  for x in range(w, qx, -1):
    for y in range(h, qy, -1):
      print(x,y)
      q4 += len(grid[(x,y)])

  print(q1,q2,q3,q4)
  return q1*q2*q3*q4


SAMPLE_INPUT = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


print("sample input: ", solve(SAMPLE_INPUT))

with open("day14/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


