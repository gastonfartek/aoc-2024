from collections import defaultdict

def solve(input_str: str):

  result = 0
  a = []
  b = defaultdict(int)

  for line in input_str.splitlines():

    left,right = line.split('   ')
    a.append(int(left))
    b[int(right)] += 1


  for n in a:
    result += n * b[n]


  return result



SAMPLE_IMPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""

print("sample input: ", solve(SAMPLE_IMPUT))

with open("input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))