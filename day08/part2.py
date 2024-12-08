from collections import defaultdict

def solve(input_str: str):
  result = 0
  antennas = defaultdict(list)
  s = set()
  lines = input_str.splitlines()
  n = len(lines)
  m = len(lines[0])

  for y in range(n):
     for x in range(m):

        c = lines[y][x]

        if c != '.':
          for xx,yy in antennas[c]:
             diff_x = abs(xx-x)
             diff_y = abs(yy-y)

             antinode_1 = [1 if x > xx else -1, 1, x, y]
             s.add((x,y))

             while True:
              antinode_1[2] += (diff_x * antinode_1[0])
              antinode_1[3] += (diff_y * antinode_1[1])
              if not (antinode_1[2] in range(m) and antinode_1[3] in range(n)):
                 break

              s.add((antinode_1[2], antinode_1[3]))


             antinode_2 = [1 if xx > x else -1, -1, xx, yy]
             s.add((xx,yy))
             while True:
              antinode_2[2] += (diff_x * antinode_2[0])
              antinode_2[3] += (diff_y * antinode_2[1])

              if not (antinode_2[2] in range(m) and antinode_2[3] in range(n)):
                break

              s.add((antinode_2[2], antinode_2[3]))



          antennas[c].append((x,y))




  return len(s)


# SAMPLE_IMPUT = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

SAMPLE_IMPUT = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day08/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))