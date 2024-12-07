from itertools import product

def solve(input_str: str):
  result = 0

  for line in input_str.splitlines():
    test_value, numbers = line.split(': ')
    test_value = int(test_value)
    numbers = list(map(int, numbers.split()))


    operations = product("+*", repeat=len(numbers)-1)

    for o in operations:
      total = numbers[0]

      for i in range(len(o)):

        if o[i] == '+':
          total += numbers[i+1]
        else:
          total *= numbers[i+1]

        if total > test_value:
          break


      if total == test_value:
        result += test_value
        break

  return result



SAMPLE_IMPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day07/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))