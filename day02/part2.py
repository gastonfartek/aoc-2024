def get_diff_and_orientation(a,b):
   return (abs(a - b), 'd' if a > b else 'i')

def is_safe(levels):

  prev_orientation = None
  for i in range(len(levels) - 1):
    diff, o = get_diff_and_orientation(levels[i], levels[i+1])

    if (prev_orientation is not None and o != prev_orientation) or not 0 < diff <= 3:
      return False

    prev_orientation = o

  return True

def solve(input_str: str):

  result = 0

  for line in input_str.splitlines():

    levels = [int(n) for n in line.split()]

    if is_safe(levels):
      result += 1
    else:
      for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i+1:]):
          result += 1
          break


  return result



SAMPLE_IMPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

print("sample input: ", solve(SAMPLE_IMPUT))

with open("day02/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))