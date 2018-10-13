MAX_V = int(1e5) # たぶんVでよい

V = 0 # 頂点数
G = [0]*MAX_V # グラフの隣接リスト表現
for i in range(MAX_V):
    G[i] = []
match = [-1]*MAX_V # マッチングのペア
used = [False]*MAX_V # DFSで既に調べたかのフラグ

# uとvを結ぶ辺をグラフに追加する
def addEdge(u, v):
    G[u].append(v)
    G[v].append(u)



# 増加パスをDFSで探す
def dfs(v):
    used[v] = True
    for i in range(len(G[v])):
        u = G[v][i]
        w = match[u]
        if w < 0 or not used[w] and dfs(w):
            match[v] = u
            match[u] = v
            return True
    return False

# 二部グラフの最大マッチングを求める
def bipartiteMatching():
    res = 0
    for v in range(V):
        if match[v] < 0:
            for i in range(len(used)):
                used[i] = False
            if dfs(v):
                res += 1
    return res
