def solve(input_str: str):
  result = 0

  l = {}
  free_spaces = []
  id = 0
  is_number = True
  i = 0
  for s in input_str:
    n = int(s)

    if is_number:
      l[id]= (i, n)
      id +=1
      is_number = False
    else:
      if n > 0:
        free_spaces.append((i, n))
      is_number = True
    i += n

  for i in reversed(l.keys()):

    for ii, v in enumerate(free_spaces):
      free_space_index, free_space_length = v
      if free_space_index >= l[i][0]:
        break


      diff = free_space_length - l[i][1]

      if diff == 0:
        l[i] = (free_space_index, free_space_length)
        del free_spaces[ii]
        break


      if diff > 0:
        l[i] = (free_space_index, l[i][1])
        free_spaces[ii] = (free_space_index + l[i][1], diff)
        break


  for k, v in l.items():
    for n in range(v[1]):
      result += (v[0] + n) * k

  return result



SAMPLE_IMPUT = """2333133121414131402"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day09/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))