# O(V^3)
# V は頂点数
d = makelist(V, V)  # d[a][b] は辺 e = (a, b) のコスト(存在しない場合はINF, ただし d[i][i] = 0 とする)

MAX = int(1e9)
# 初期化
for i in range(V):
    for j in range(V):
        if i == j:
            d[i][j] = 0
        else:
            d[i][j] = MAX

# ここで d の入力行う

# function
def warshall_floyd():
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
