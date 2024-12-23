from heapq import heapify, heappop
from itertools import permutations, product

def create_movement_map(coordinates, restricted_coord):

    movements = {
        (0, 1): ">", (0, -1): "<",
        (1, 0): "v", (-1, 0): "^"
    }

    movement_map = {}

    for start_key, start_coord in coordinates.items():
        movement_map[start_key] = {}
        for end_key, end_coord in coordinates.items():
            if start_key == end_key:
                movement_map[start_key][end_key] = []
                continue

            horizontal_moves = []
            vertical_moves = []

            # Calculate horizontal and vertical moves needed
            horizontal_diff = end_coord[1] - start_coord[1]
            vertical_diff = end_coord[0] - start_coord[0]

            if horizontal_diff > 0:
                horizontal_moves.extend([movements[(0, 1)]] * horizontal_diff)
            elif horizontal_diff < 0:
                horizontal_moves.extend([movements[(0, -1)]] * -horizontal_diff)

            if vertical_diff > 0:
                vertical_moves.extend([movements[(1, 0)]] * vertical_diff)
            elif vertical_diff < 0:
                vertical_moves.extend([movements[(-1, 0)]] * -vertical_diff)

            all_moves = horizontal_moves + vertical_moves
            unique_paths = set()

            for path in permutations(all_moves):
                current_position = list(start_coord)
                valid_path = True

                for move in path:
                    if move == ">":
                        current_position[1] += 1
                    elif move == "<":
                        current_position[1] -= 1
                    elif move == "v":
                        current_position[0] += 1
                    elif move == "^":
                        current_position[0] -= 1

                    if current_position == list(restricted_coord):
                        valid_path = False
                        break

                if valid_path:
                    unique_paths.add(path)

            # Store each unique path as a list
            movement_map[start_key][end_key] = [list(path) for path in unique_paths]

    return movement_map




def solve(input_str: str):
  m = [list(l) for l in input_str.splitlines()]

  dirs = {
     (0,1): '>',
     (0,-1): '<',
     (-1,0): '^',
     (1,0): 'v',
    #  (0,0): 'A'
  }


  keypad_map = create_movement_map({
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "0": (3, 1), "A": (3, 2)
  }, (3, 0))

  dir_map = create_movement_map({
      "^": (0, 1), "A": (0, 2),
      "<": (1, 0), "v": (1, 1), ">": (1, 2)
  }, (0,0))

  result = 0

  for code in input_str.splitlines():

    pos = 'A'
    robot1 = [[]]
    for c in code:
      n = []
      m = keypad_map[pos][c]
      for item in m:
          for r in robot1:
            n.append(r+item + ["A"])

      robot1 = n
      pos = c

    pos = "A"
    robot2 = []
    for rm in robot1:
        temp = [[]]
        for m in rm:
          n = []
          dirs = dir_map[pos][m]

          for d in dirs:
            for robot_instance in temp:
              n.append(robot_instance + d + ['A'])

          if len(n) == 0:
              temp = [r + ["A"] for r in temp]
          else:
            shortest = min(map(len, n))
            temp = [dirs for dirs in n if len(dirs) == shortest]

          pos = m

        robot2 += temp



    pos = "A"
    robot3 = []
    for rm in robot2:
        temp = [[]]
        for m in rm:
          n = []
          dirs = dir_map[pos][m]

          for d in dirs:
            for robot_instance in temp:
              n.append(robot_instance + d + ['A'])

          if len(n) == 0:
              temp = [r + ["A"] for r in temp]
          else:
            shortest = min(map(len, n))
            temp = [dirs for dirs in n if len(dirs) == shortest]

          pos = m

        robot3 += temp
    robot3 = sorted(robot3, key=len)
    print(len(robot3[0]), int("".join(code[:3])))
    result += len(robot3[0]) * int("".join(code[:3]))

  return result



SAMPLE_INPUT = """029A
980A
179A
456A
379A"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day21/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


