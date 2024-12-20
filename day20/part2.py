from collections import defaultdict
from heapq import heappush, heappop
import pprint

def solve(input_str: str):

  m = [list(l) for l in input_str.splitlines()]

  start = None
  w = len(m)
  h = len(m[0])

  for y in range(len(m)):
    for x in range(len(m[y])):
      if m[y][x] == 'S':
        start = (y,x)


  pos = start
  visited = set()
  base = 0
  path = {}
  while True:
    path[pos] = base

    if m[pos[0]][pos[1]] == 'E':
      break
    visited.add(pos)


    for y,x in [(-1,0),(0,1),(1,0),(0,-1)]:
      next_pos = (pos[0] + y, pos[1] + x)
      if m[next_pos[0]][next_pos[1]] != '#' and next_pos not in visited:
        pos = next_pos
        base += 1
        break


  result = 0
  for y,x in path.keys():
    for i in range (2,21):
      for j in range(i+1):
        c = i - j
        for nr,nc in set([(y + j,x + c),(y + j,x - c), (y - j, x+c), (y-j, x-c)]):
          if nr in range(h) and nc in range(w) and (nr,nc) in path:
            result += 1 if path[(y,x)] - path[(nr,nc)] >= 100 + i else 0


  return result



SAMPLE_INPUT = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day20/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


