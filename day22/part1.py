from heapq import heapify, heappop
from itertools import permutations, product

def calculate(n):
    # seen_states = {}
    i = 0

    while i < 2000:
        # if n in seen_states:
        #     # Cycle
        #     cycle_start = seen_states[n]
        #     cycle_length = i - cycle_start
        #     remaining_iterations = (2000 - i) % cycle_length
        #     # Fast forward
        #     for _ in range(remaining_iterations):
        #         n = perform_operations(n)
        #     return n

        # Record the current state
        # seen_states[n] = i
        # print(i)
        # Perform the operations
        n = perform_operations(n)
        i += 1

    return n
def perform_operations(n):
    o = n
    n = n * 64
    n = o ^ n
    n = n % 16777216
    o = n // 32
    n = o ^ n
    n = n % 16777216
    o = n * 2048
    n = o ^ n
    n = n % 16777216
    return n

def solve(input_str: str):

  nums = list(map(int, input_str.splitlines()))

  result = [calculate(n) for n in nums]

  return sum(result)



SAMPLE_INPUT = """123"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day22/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))