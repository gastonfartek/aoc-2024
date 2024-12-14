def solve(input_str: str):
  result = 0

  l = []

  for line in input_str.split('\n\n'):
    game = line.splitlines()
    a = game[0].replace('Button A: X+','').replace(', Y+', ' ').split()
    b = game[1].replace('Button B: X+','').replace(', Y+', ' ').split()
    p = game[2].replace('Prize: X=','').replace(', Y=', ' ').split()
    l.append((
      (int(a[0]), int(a[1])),
      (int(b[0]), int(b[1])),
      (int(p[0]), int(p[1])),
    ))

  result = 0
  for game in l:

    a,b,p = game
    prize_x ,prize_y = p
    prize_x += 10000000000000
    prize_y += 10000000000000
    r = None

    for i in range(100):
      for j in range(100):
        x = a[0] * i + b[0] * j
        y = a[1] * i + b[1] * j
        if x == prize_x and y == prize_y:
          r = min(r, 3*i+j) if r is not None else 3*i + j



    result += r if r is not None else 0


  return result



SAMPLE_IMPUT = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day13/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


