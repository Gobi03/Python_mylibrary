# 要テスト

# O(E log(E))
import heapq

MAX = int(1e9)

# V は頂点数
# input
cost = makelist(V, V)  # cost[a][b]  a から b へのコスト(存在しない時は MAX を入れる)
for i in range(V):
	for j in range(V):
		cost[i][j] = MAX


mincost = [MAX]*V      # 集合 X からの辺の最小コスト
used = [False]*V       # 頂点 i が X に含まれているか
pq = []                # (cost, node)

def prim():
	# 初期準備
	mincost[0] = 0
	res = 0
	heapq.heappush(pq, (0, 0))

	while True:
		now = -1

		# X に属さない頂点のうち X からの辺のコストが最小になる頂点を探す
		while len(pq) != 0:
			ind = heapq.heappop(q)[1]
			if not used[ind]:
				now = ind
				break

		if now == -1:  # 全部つなぎ終わったら抜ける(終了条件)
			break

		used[now] = True  # 頂点 now を X に追加
		res += mincost[now]  # 辺のコストを加える

		# 今回追加した頂点からのコストをmincostに加味する(次のループへの準備)
		for i in range(V):
			if mincost[i] < cost[now][i]:
				mincost[i] = cost[now][i]
				heapq.heappush(pq, (cost[now][i], i))

	return res
