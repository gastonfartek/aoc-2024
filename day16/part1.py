from collections import defaultdict
from heapq import heappush, heappop


def solve(input_str: str):
  result = 0

  start = None
  end = None

  m = [list(line) for line in input_str.splitlines()]
  print(m)

  h = len(m)
  l = len(m[0])
  for i, line in enumerate(m):
     for j, l in enumerate(line):
        if l == 'S':
          start = (i,j)

        if l =='E':
          end = (i,j)


  q = []
  heappush(q, (0, start, (0,1)))
  visited = {}
  # heappush(q, (1000, start, (-1,0)))
  # heappush(q, (1000, start, (1,0)))

  while len(q):
    cost, pos, dir = heappop(q)

    if pos == end:
      result = cost
      break

    if (pos,dir) in visited.keys() and visited[(pos,dir)]<= cost:
      continue

    visited[(pos,dir)] = cost

    for y,x in [(-1,0),(0,1),(1,0),(0,-1)]:

      if (y*-1,x*-1) == dir:
        continue

      next_y = pos[0]+y
      next_x = pos[1]+x

      if m[next_y][next_x] == '#':
        continue

      c = 1

      if dir[0] != 0 and x != 0 or dir[1] != 0 and y != 0:
        c += 1000

      heappush(q, (cost+c, (next_y, next_x), (y,x)))


  return result


SAMPLE_INPUT = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

# SAMPLE_INPUT = """#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day16/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


