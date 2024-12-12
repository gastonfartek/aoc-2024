from collections import deque



def solve(input_str: str):
  result = 0

  matrix = []

  possible_trails = []
  for i, line in enumerate(input_str.splitlines()):
    temp = []
    for j, value in enumerate(line):
      if value == '0':
          possible_trails.append((i,j))

      temp.append(int(value))

    matrix.append(temp)

  max_y = len(matrix)
  max_x = len(matrix[0])

  def score(coords):
     q = deque()

     q.append(coords)
     total = 0
     while len(q):
      i,j = q.popleft()

      v = matrix[i][j]

      if v == 9:
        print('found')
        total += 1

      for y, x in [(1,0), (0,1), (-1,0), (0, -1)]:
        n_i = i + y
        n_j = j + x
        if n_i in range(max_y) and n_j in range(max_x) and matrix[n_i][n_j] == matrix[i][j] + 1:
          q.append((i + y, j + x))

     return total

  for coord in possible_trails:
    result += score(coord)

  return result



SAMPLE_IMPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day10/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))