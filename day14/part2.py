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
  robots = 0
  for line in input_str.split('\n'):
    line = line.replace('p=','').replace('v=','').split()
    pos = line[0].split(',')
    v = line[1].split(',')
    robots += 1
    grid[(int(pos[0]), int(pos[1]))].append((int(v[0]), int(v[1])))

  i = 0
  while True:
    i += 1
    new_grid = defaultdict(list)
    for key, v in grid.items():
      while len(v):
        robot = v.pop()
        x = (key[0] + robot[0]) % w
        y = (key[1] + robot[1]) % h
        new_grid[(abs(x), abs(y))].append(robot)

    grid = new_grid
    if len(grid.keys()) == robots:
      break

  with open('output.txt', 'a') as f:
    for yy in range(h):
      for xx in range(x):
        f.write('#' if (xx,yy) in grid else '.')
      f.write('\n')

  return i


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

"""
.....#2..1.
...........
1..........
.11........
.....1.....
...12......
.1....1...."""


# print("sample input: ", solve(SAMPLE_INPUT))

with open("day14/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


