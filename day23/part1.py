from collections import defaultdict
from itertools import product

def solve(input_str: str):

    result = 0

    adj_list = defaultdict(list)

    for l in input_str.splitlines():
        a,b = l.split('-')
        adj_list[a].append(b)


    result = set()
    for k in adj_list.keys():
        for i,j in product(range(len(adj_list[k])), repeat=2):

            a = adj_list[k][i]
            b = adj_list[k][j]

            for aa in adj_list[a]:
                if k in adj_list[aa] or b == aa:
                    if k[0] == 't' or a[0] == 't' or aa[0] == 't':
                        result.add(tuple(sorted([k,a,aa])))
            for bb in adj_list[b]:
                if k in adj_list[bb] or a == bb:
                    if k[0] == 't' or b[0] == 't' or bb[0] == 't':
                        result.add(tuple(sorted([k,b,bb])))



    return len(result)


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