def solve(input_str: str):

  a, b = input_str.split('\n\n')

  towels = set(a.split(", "))

  cache = {}
  def count(s: str):
    if s in cache:
     return cache[s]

    if len(s) == 0:
      return 1

    result = 0
    for t in towels:
      if s.startswith(t):
        result += count(s[len(t):])
    cache[s] = result
    return result

  ans = 0
  for design in b.splitlines():
    ans += count(design)


  return ans


SAMPLE_INPUT = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

print("sample input: ", solve(SAMPLE_INPUT, 6, 12))

with open("day19/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read(), 70, 1024))


