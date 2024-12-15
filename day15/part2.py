from collections import defaultdict
from math import floor

def solve(input_str: str):
  result = 0
  a,b = input_str.split("\n\n")
  moves = []
  for c in b.splitlines():
    moves += list(c)

  m = []
  pos = None
  for i, line,  in enumerate(a.splitlines()):
    m.append([])
    j = 0
    for c in line:
      if c == '@':
         m[i].append('@')
         j += 1
         m[i].append('.')
         j += 1
      elif c == 'O':
        m[i].append(((i,j), (i,j+1)))
        m[i].append(((i,j), (i,j+1)))
        j += 2
      else:
        m[i].append(c)
        j += 1
        m[i].append(c)
        j += 1

  for ii in range(len(m)):
    for jj in range(len(m[0])):
      if m[ii][jj] == '@':
        pos = (ii,jj)
        break

  moves_map = {
     '^': (-1,0),
     '>': (0,1),
     'v': (1,0),
     '<': (0,-1),
  }

  for move_type in moves:
    move = moves_map[move_type]
    next_pos = (pos[0] + move[0], pos[1] + move[1])

    if m[next_pos[0]][next_pos[1]] == '.':
       m[pos[0]][pos[1]] = '.'
       m[next_pos[0]][next_pos[1]] = '@'
       pos = next_pos
    elif m[next_pos[0]][next_pos[1]] == '#':
      continue
    else:

      target_pos = None

      if move_type == '<' or move_type == '>':
        while m[next_pos[0]][next_pos[1]] != '.':
          next_pos = (next_pos[0] + move[0], next_pos[1] + move[1])
          if next_pos[0] not in range(len(m)) or next_pos[1] not in range(len(m[0])):
            break

          if m[next_pos[0]][next_pos[1]] == '#':
            break

          if m[next_pos[0]][next_pos[1]] == '.':
            target_pos = next_pos

        if target_pos is not None:
          n_move = (move[0] * -1, move[1] * -1)
          while target_pos != pos:
            n = (target_pos[0] + n_move[0], target_pos[1] + n_move[1])
            m[target_pos[0]][target_pos[1]] = m[n[0]][n[1]]

            if m[target_pos[0]][target_pos[1]] != '@':
              a,b = m[target_pos[0]][target_pos[1]]
              m[target_pos[0]][target_pos[1]] = ((a[0] + move[0], a[1] + move[1]), (b[0] + move[0], b[1] + move[1]))
              target_pos = (target_pos[0] + n_move[0], target_pos[1] + n_move[1])
              n = (target_pos[0] + n_move[0], target_pos[1] + n_move[1])
              a,b = m[target_pos[0]][target_pos[1]]
              m[target_pos[0]][target_pos[1]] = ((a[0] + move[0], a[1] + move[1]), (b[0] + move[0], b[1] + move[1]))

            target_pos = (target_pos[0] + n_move[0], target_pos[1] + n_move[1])
            m[n[0]][n[1]] = "."

          # m[pos[0]][pos[1]] = '.'
          pos = (pos[0] + move[0], pos[1] + move[1])
      else:
        coords = [[ coord for coord in m[next_pos[0]][next_pos[1]]]]
        while True:

          do = True
          new_coords = []
          for c in coords[-1]:
            next_pos = (c[0] + move[0], c[1] + move[1])
            if next_pos[0] not in range(len(m)) or next_pos[1] not in range(len(m[0])):
              do = False
              coords = []
              break

            if m[next_pos[0]][next_pos[1]] == '#':
              do = False
              coords = []
              break

            if m[next_pos[0]][next_pos[1]] != '.' and m[next_pos[0]][next_pos[1]][0] not in new_coords:
              new_coords.append(m[next_pos[0]][next_pos[1]][0])
              new_coords.append(m[next_pos[0]][next_pos[1]][1])

          if do and len(new_coords):
            coords.append(new_coords)
          else:
            break

        for i in range(len(coords) -1, -1, -1):
          for c in coords[i]:
            n = (c[0] + move[0], c[1] + move[1])

            a,b = m[c[0]][c[1]]
            m[n[0]][n[1]] = ((a[0] + move[0], a[1] + move[1]), (b[0] + move[0], b[1] + move[1]))
            m[c[0]][c[1]] = '.'

        if len(coords):
          m[pos[0]][pos[1]] = '.'
          pos = (pos[0] + move[0], pos[1] + move[1])
          m[pos[0]][pos[1]] = '@'








  seen = set()
  for y in range(len(m)):
    for x in range(len(m[0])):
      if m[y][x] != '@' and m[y][x] != '.' and m[y][x] != '#' and m[y][x] not in seen:
        seen.add(m[y][x])
        print(m[y][x])
        a,b = m[y][x]
        result += (a[0] * 100) + a[1]



  return result


SAMPLE_INPUT = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# SAMPLE_INPUT = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day15/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


