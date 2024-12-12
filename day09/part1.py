def solve(input_str: str):
  result = 0

  l = []

  length = 0
  id = 0
  is_number = True
  for s in input_str:
    n = int(s)
    k = id if is_number else '.'
    l += [k] * n

    if is_number:
      id +=1
      is_number = False
    else:
      is_number = True

  i = 0
  j = len(l) - 1

  while j > i:

    if l[i] != '.' or l[j] == '.':
      while i < j and l[i] != '.':
        i += 1

      while i < j and l[j] == '.':
        j -= 1

      continue

    l[i] = l[j]
    del l[j]
    j -= 1

  for i, n in enumerate(l):
    if n == '.':
      break

    result += i * n

  return result



SAMPLE_IMPUT = """2333133121414131402"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day09/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))