

def solve(input_str: str):

  result = 0
  a = []
  b = []

  for line in input_str.splitlines():

    left,right = line.split('   ')
    a.append(int(left))
    b.append(int(right))

  a.sort()
  b.sort()

  for i in range(len(a)):
    result += abs(a[i] - b[i])

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