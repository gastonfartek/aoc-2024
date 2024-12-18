from collections import defaultdict
from heapq import heappush, heappop


def solve(input_str: str):
  result = 0
  registers, program = input_str.split("\n\n")

  registers = list(map(int, (r.split(": ")[1] for r in registers.splitlines())))
  program = list(map(int, program.replace("Program: ","").split(',')))

  result = []
  i = 0
  while i + 1 < len(program):
    opcode = program[i]
    literal_operand = program[i+1]

    combo_operand = literal_operand if literal_operand <=3 or literal_operand == 7 else registers[literal_operand-4]

    if opcode == 0:
      registers[0] = registers[0] // (pow(2,combo_operand))
    if opcode == 1:
      registers[1] = registers[1] ^ literal_operand
    if opcode == 2:
      registers[1] = combo_operand % 8
    if opcode == 3 and registers[0] != 0:
      i = literal_operand
      continue
    if opcode == 4:
      registers[1] = registers[1] ^ registers[2]
    if opcode == 5:
      result.append(combo_operand % 8)
    if opcode == 6:
      registers[1] = registers[0] // (pow(2,combo_operand))
    if opcode == 7:
      registers[2] = registers[0] // (pow(2,combo_operand))

    i += 2

  return ",".join(map(str,result))


SAMPLE_INPUT = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day17/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))


