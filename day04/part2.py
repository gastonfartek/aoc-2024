from collections import Counter

def solve(input_str: str):
  result = 0
  m = [line for line in input_str.splitlines()]

  maxY = len(m)
  maxX = len(m[0])

  for y in range(maxY):
    for x in range(maxX):

      if m[y][x] != 'A':
         continue

      if y - 1 < 0 or y + 1 >= maxY or x - 1 < 0 or x + 1 >= maxX:
         continue

      c = Counter(m[y-1][x-1] + m[y-1][x+1] + m[y+1][x + 1] + m[y+1][x - 1])

      result += 1 if c['S'] == 2 and c['M'] == 2 and m[y-1][x-1] != m[y+1][x+1] else 0

  return result



SAMPLE_IMPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day04/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))