def solve(input_str: str):
  result = 0
  m = [line for line in input_str.splitlines()]

  maxY = len(m)
  maxX = len(m[0])

  d = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]

  for y in range(maxY):
    for x in range(maxX):
      for yy, xx in d:
        if 0 <= y + 3 * yy < maxY and 0 <= x + 3 * xx < maxX:
          w = m[y][x]
          w += m[y + 1 * yy][x + 1 * xx]
          w += m[y + 2 * yy][x + 2 * xx]
          w += m[y + 3 * yy][x + 3 * xx]
          result += 1 if w == 'XMAS' else 0

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