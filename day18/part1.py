from collections import deque


def solve(input_str: str, s: int, length: int):
  result = float("inf")
  l = [tuple(map(int,l.split(','))) for l in input_str.splitlines()]
  bytes = set(l[:length])

  visited = {}
  q = deque()
  q.append(((0,0),0))

  while len(q):
    pos, c = q.popleft()

    x,y = pos

    if x == s and y == s:
      result = min(result, c)
      continue

    if pos in visited and visited[pos] <= c:
      continue

    visited[pos] = c


    for ny, nx in ((1,0), (-1,0), (0,1), (0,-1)):
      next_pos = (x + nx, y + ny)
      if 0 <= next_pos[0] <= s and 0 <= next_pos[1] <= s and next_pos not in bytes:
        q.append((next_pos, c + 1))

  return result


SAMPLE_INPUT = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

print("sample input: ", solve(SAMPLE_INPUT, 6, 12))

with open("day18/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read(), 70, 1024))


