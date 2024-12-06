from collections import defaultdict

def solve(input_str: str):
  result = 0

  data = input_str.split('\n\n')

  ordering_rules = defaultdict(list)

  for rule in data[0].splitlines():
    before, after = rule.split('|')
    ordering_rules[int(after)].append(int(before))

  invalid_updates = []

  for line in data[1].splitlines():

    pages = list(map(int,line.split(',')))
    total_pages_set = set(pages)

    is_valid = True

    for i in range(len(pages) - 1, -1, -1):
      s = set(pages[:i])

      for rule in ordering_rules[pages[i]]:
        if rule in total_pages_set and rule not in s:
          is_valid = False
          break

      if not is_valid:
        break

    if not is_valid:
      invalid_updates.append(pages)


  r = []
  for rule in data[0].splitlines():
    a,b = rule.split('|')
    r.append((int(a), int(b)))


  for update in invalid_updates:
    while True:
      is_sorted = True
      for i in range(len(update) - 1):
        if (update[i+1], update[i]) in r:
          is_sorted = False
          update[i], update[i+1] = update[i+1], update[i]

      if is_sorted:
        result += update[len(update) // 2]
        break



  return result



SAMPLE_IMPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


print("sample input: ", solve(SAMPLE_IMPUT))

with open("day05/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))