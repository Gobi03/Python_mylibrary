# O(E log|V|)
# V は頂点数
# E はノード数


## Union-Find
uni = [-1]*V

def root(v):
    if uni[v] < 0:  # v が親の場合
        return v
    else:           # v が子の場合
        uni[v] = root(uni[v])  # 親のrootを調べる
        return uni[v]

# 頂点 a と頂点 b をつなぐ。もともと同じグループのとき、False を返す
def connect(a, b):
    # まずはそれぞれ根の番号に置き換える
    ra = root(a)
    rb = root(b)
    if ra == rb:
        return False
    
    # ra を大きなグループにしたいので、逆であれば入れ替える
    if uni[ra] > uni[rb]: # rbの方が要素数が多ければ
        tmp = ra
        ra  = rb 
        rb  = tmp
        
    # ra と rb を結合し、rb の親を ra とする
    uni[ra] += uni[rb]
    uni[rb] = ra
    return True

# 頂点 a, b が同じグループであるかを調べる
def isConnect(a, b):
    return root(a) == root(b)



## Kruskal法
# edge は cost, from, to のタプルで表す
edges = [(0, 0, 0)]*E

# edges 入力

def kruskal():
    edges.sort()  # edge のコストが小さい順にソートする

    res = 0
    for ed in edges:
        if not isConnect(ed[1], ed[2]):
            connect(ed[1], ed[2])
            res += ed[0]

    return res
