import itertools as it
from itertools import combinations

m = ['a1','a1','a1','a1','a2','a2','a2','a2','a2','a2','a2','a2']
n = ['b1','b1','b1','b1','b1','b1','b1','b2','b2','b2','b2','b2','b2','b2','b2','b2']


def main(m, n):
    c = len(list(it.product(m, n)))
    d = [",".join(map(str, comb)) for comb in combinations(m, n, 2)]
    print(d)

if __name__ == '__main__':
    main(m,n)