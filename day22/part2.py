from collections import defaultdict

def perform_operations(n):
    o = n
    n = n * 64
    n = o ^ n
    n = n % 16777216
    o = n // 32
    n = o ^ n
    n = n % 16777216
    o = n * 2048
    n = o ^ n
    n = n % 16777216
    return n

def solve(input_str: str):

  nums = list(map(int, input_str.splitlines()))
  seq = defaultdict(int)
  for n in nums:
      i = 0
      numbers = []
      seen = set()

      while i < 2000:
          numbers.append(n % 10)
          if len(numbers) > 4:
            a,b,c,d,e = numbers[i-4:i+1]

            s = (b-a,c-b,d-c,e-d)

            if s not in seen:
                seq[s] += e

            seen.add(s)

          n = perform_operations(n)
          i += 1

  return max(*seq.values())



SAMPLE_INPUT = """1
2
3
2024"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day22/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))