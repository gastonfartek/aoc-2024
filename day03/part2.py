import re

def solve(input_str: str):
  result = 0

  mul = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", input_str)

  do = True
  for n in mul:
     if do and n[2] == "":
        result += int(n[0]) * int(n[1])
     else:
        do = True if n[2] == 'do()' else False

  return result


SAMPLE_IMPUT = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

print("sample input: ", solve(SAMPLE_IMPUT))

with open("day03/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))