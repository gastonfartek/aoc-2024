# from collections import defaultdict, deque
# from heapq import heappush, heappop


# def solve(input_str: str):
#   result = 0

#   start = None
#   end = None

#   m = [list(line) for line in input_str.splitlines()]

#   h = len(m)
#   l = len(m[0])
#   for i, line in enumerate(m):
#      for j, l in enumerate(line):
#         if l == 'S':
#           start = (i,j)

#         if l =='E':
#           end = (i,j)


#   q = []
#   lowest = None

#   heappush(q, (0, start, (0,1), set()))
#   final_s = set()
#   visited = {}
#   while len(q):
#     cost, pos, dir, s = heappop(q)

#     if lowest is not None and cost > lowest:
#       continue

#     if pos == end:
#       if lowest is None or cost == lowest:
#         lowest = cost
#         final_s = final_s.union(s)

#     # if (pos,dir) in visited.keys() and visited[(pos,dir)]<= cost:
#     #   continue
#     if pos in s:
#       continue

#     visited[(pos,dir)] = cost
#     s.add(pos)
#     for y,x in [(-1,0),(0,1),(1,0),(0,-1)]:

#       if (y*-1,x*-1) == dir:
#         continue

#       next_y = pos[0]+y
#       next_x = pos[1]+x

#       if m[next_y][next_x] == '#':
#         continue

#       c = 1

#       if dir[0] != 0 and x != 0 or dir[1] != 0 and y != 0:
#         c += 1000

#       heappush(q, (cost+c, (next_y, next_x), (y,x), set(s)))

#   print(sorted(final_s))
#   return len(final_s)






# (8, 3),



# (9, 1),
# (9, 2),
# (9, 3),



# (10, 1),
# (10, 3),












# SAMPLE_INPUT = """###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############"""

# # SAMPLE_INPUT = """#################
# # #...#...#...#..E#
# # #.#.#.#.#.#.#.#.#
# # #.#.#.#...#...#.#
# # #.#.#.#.###.#.#.#
# # #...#.#.#.....#.#
# # #.#.#.#.#.#####.#
# # #.#...#.#.#.....#
# # #.#.#####.#.###.#
# # #.#.#.......#...#
# # #.#.###.#####.###
# # #.#.#...#.....#.#
# # #.#.#.#####.###.#
# # #.#.#.........#.#
# # #.#.#.#########.#
# # #S#.............#
# # #################"""

# print("sample input: ", solve(SAMPLE_INPUT))

# # with open("day16/input.txt", "r") as input_file:
# #     print("input: ", solve(input_file.read()))


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
  lowest = None
  while len(q):
    cost, pos, dir = heappop(q)

    if pos == end:
      lowest = cost
      break

    if (pos,dir) in visited.keys() and visited[(pos,dir)]<= cost:
      continue

    visited[(pos, dir)] = cost

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



  q = []
  heappush(q, (0, start, (0,1), set()))
  final_s = set()
  while len(q):
    cost, pos, dir, s = heappop(q)
    print(len(q))

    if pos == end:
      final_s = final_s.union(s)

    # if (pos,dir) in visited.keys():
    #   if visited[(pos,dir)] == cost:
    #     final_s = final_s.union(s)
    #   continue

    s.add(pos)
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
      if cost+c <= lowest and (next_y, next_x) not in s:
        heappush(q, (cost+c, (next_y, next_x), (y,x), type(s)(s)))



  return len(final_s)


# SAMPLE_INPUT = """###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############"""

SAMPLE_INPUT = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day16/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


