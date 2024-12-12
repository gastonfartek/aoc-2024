from functools import cache

def solve(input_str: str):
  result = 0

  stones = input_str.split()

  for i in range(25):

    temp = []
    for s in stones:
      if s == '0':
        temp.append('1')
        continue

      if len(s) % 2 == 0:
        middle = len(s) // 2
        temp.append(str(int(s[:middle])))
        temp.append(str(int(s[middle:])))
        continue

      temp.append(str(int(s) * 2024))

    stones = temp




  return len(stones)



SAMPLE_IMPUT = """125 17"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day11/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


