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
    for j, c in enumerate(line):
      m[i].append(c)
      if c == '@':
         pos = (i,j)

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

    if m[next_pos[0]][next_pos[1]] == 'O':

      target_pos = None
      #  new_m = m
      while m[next_pos[0]][next_pos[1]] != '.':
        next_pos = (next_pos[0] + move[0], next_pos[1] + move[1])
        if next_pos[0] not in range(len(m)) or next_pos[1] not in range(len(m[0])):
          break

        if m[next_pos[0]][next_pos[1]] == '.':
          target_pos = next_pos
        elif m[next_pos[0]][next_pos[1]] == '#':
          break

      if target_pos is not None:
        n_move = (move[0] * -1, move[1] * -1)
        while target_pos != pos:
          n = (target_pos[0] + n_move[0], target_pos[1] + n_move[1])
          m[target_pos[0]][target_pos[1]] = m[n[0]][n[1]]
          m[n[0]][n[1]] = '.'
          target_pos = (target_pos[0] + n_move[0], target_pos[1] + n_move[1])

        # m[pos[0]][pos[1]] = '.'
        pos = (pos[0] + move[0], pos[1] + move[1])
        # m[pos[0]][pos[1]] = '@'






      #  temp = next_pos
      #  can_move = False
      #  while m[temp[0]][temp[1]] != '.':
      #     n = (temp[0] + move[0], temp[1] + move[1])
      #     if m[n[0]][n[1]] == '.':





  for y in range(len(m)):
    for x in range(len(m[0])):
      if m[y][x] == 'O':
        result += (y * 100) + x


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

# SAMPLE_INPUT = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day15/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


