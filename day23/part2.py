from collections import defaultdict, deque
from itertools import product

def solve(input_str: str):

    adj_list = defaultdict(set)

    for l in input_str.splitlines():
        a, b = l.split('-')
        adj_list[a].add(b)
        adj_list[b].add(a)

    largest = set()

    for node in adj_list:
        for neighbor in adj_list[node]:
            c = {node, neighbor}

            for other in adj_list[node]:
                if other in adj_list[neighbor]:
                    c.add(other)

            if all(other in adj_list[neighbor] for neighbor in c for other in c if other != neighbor):
                if len(c) > len(largest):
                    largest = c

    return ",".join(sorted(largest))

SAMPLE_INPUT = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

print("sample input: ", solve(SAMPLE_INPUT))

with open("day23/input.txt", "r") as input_file:
    print("input: ", solve(input_file.read()))