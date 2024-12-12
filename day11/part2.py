from functools import cache

# @cache
cache = {}
def blink(input, n):
  if n == 0:
    return 1

  cache_key = (input, n)
  if cache_key in cache:
    return cache[cache_key]

  result = 0
  if input == 0:
    result = blink(1, n-1)
  elif len(str(input)) % 2 == 0:
    s = str(input)
    middle = len(s) // 2
    result += blink(int(s[:middle]), n-1)
    result += blink(int(s[middle:]), n-1)
  else:
    result = blink(input * 2024, n-1)

  cache[cache_key] = result
  return result

def solve(input_str: str):
  total = 0

  stones = input_str.split()

  for s in stones:
    total += blink(int(s), 75)

  return total



SAMPLE_IMPUT = """125 17"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day11/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


