# 要テスト

# BinaryIndexedTree

N = 42
bit = [0]*(N+1)

# O(logN)
# int * int -> unit
def add(a, w):
    x = a
    while x <= N:
        bit[x] += w
        x += x & -x

# O(logN)
# int -> int
def sum(a):
    ret = 0
    x = a
    while x > 0:
        ret += bit[x]
        x -= x & -x
    return ret
