from collections import defaultdict

def solve(input_str: str):
  m = []
  pos = None
  for i, line in enumerate(input_str.split('\n')):
    m.append([c for c in line])
    if '^' in line:
      pos = (i,line.index('^'))

  maxY = len(m)
  maxX = len(m[0])

  directions = [(-1,0), (0,1), (1,0), (0,-1)]


  def run(pos):
    direction = 0

    visited = set()
    loop = False
    while 0 <= pos[0] < maxY and 0 <= pos[1] < maxX:

      posY, posX = pos
      y, x = directions[direction]

      if 0 <= posY+y < maxY and 0 <= posX+x < maxX and m[posY+y][posX+x] == '#':
        direction = (direction + 1)  % 4
        continue

      if (posY, posX, y, x) in visited:
        loop = True
        break

      visited.add((posY, posX, y, x))
      pos = (posY+y, posX+x)

    return loop

  result = 0
  for i in range(maxY):
    for j in range(maxX):
      if m[i][j] != '.':
        continue

      m[i][j] = '#'
      result += run(pos)
      m[i][j] = '.'

  return result


SAMPLE_IMPUT = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day06/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))