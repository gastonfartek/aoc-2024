import re

def solve(input_str: str):
  result = 0

  mul = re.findall(r"mul\((\d+),(\d+)\)", input_str)

  for n in mul:
     result += int(n[0]) * int(n[1])

  return result


SAMPLE_IMPUT = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

print("sample input: ", solve(SAMPLE_IMPUT))

with open("day03/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))