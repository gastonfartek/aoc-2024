from collections import deque

def solve(input_str: str):
  result = 0

  m = [list(l) for l in input_str.splitlines()]

  maxY = len(m)
  maxX = len(m[0])
  seen = set()
  q = deque()

  def find(i: int, j: int, v: str):

     plots = []
     q.append((i,j))


     while len(q):
        ii, jj = q.popleft()

        if m[ii][jj] != v or (ii,jj) in seen:
            continue

        seen.add((ii,jj))
        plots.append((ii,jj))

        if ii + 1 in range(maxY) and (ii + 1, jj) not in seen:
            q.append((ii+1, jj))

        if ii - 1 in range(maxY) and (ii - 1, jj) not in seen:
            q.append((ii-1, jj))

        if jj + 1 in range(maxX) and (ii, jj + 1) not in seen:
            q.append((ii, jj+1))

        if jj - 1 in range(maxX) and (ii, jj - 1) not in seen:
            q.append((ii, jj-1))

     return plots


  plots = []
  for i in range(len(m)):
     for j in range(len(m[0])):
        if (i,j) in seen:
           continue

        found = find(i,j,m[i][j])

        if len(found):
           plots.append(sorted(found))


  for plot in plots:
    total = 0
    for i,j in plot:
      total += 4

      for ii,jj in [(i+1,j), (i-1,j), (i,j-1),(i,j-1)]:
          if (ii,jj) in plot:
            total -= 1
    result += len(plot) * total




  return result



SAMPLE_IMPUT = """AAAA
BBCD
BBCC
EEEC"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day12/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


