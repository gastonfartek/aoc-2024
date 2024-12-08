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

             antinode_1 = (x + diff_x if x > xx else x - diff_x, y + diff_y)
             antinode_2 = (xx + diff_x if xx > x else xx - diff_x, yy - diff_y)

             if antinode_1[0] in range(m) and antinode_1[1] in range(n):
              s.add(antinode_1)

             if antinode_2[0] in range(m) and antinode_2[1] in range(n):
              s.add(antinode_2)


          antennas[c].append((x,y))




  return len(s)



SAMPLE_IMPUT = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day08/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))