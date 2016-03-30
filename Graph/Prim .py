MAX = int(1e9)

# V は頂点数
cost = makelist(V, V)  # cost[a][b]  a から b へのコスト(存在しない時は MAX を入れる)
mincost = [MAX]*V      # 集合 X からの辺の最小コスト
used = [False]*V       # 頂点 i が X に含まれているか

def prim():
	# 初期準備
	mincost[0] = 0
	res = 0

	while True:
		now = -1
		
		# X に属さない頂点のうち X からの辺のコストが最小になる頂点を探す
		for i in range(V):
			# まだ接続されていない点の中で、最も集合 X に近いものを探す
			if not used[i]:
				if now == -1:  # 最初の一点
					now = i
				elif mincost[i] < mincost[now]:
					now = i

		if now == -1:  # 全部つなぎ終わったら抜ける(終了条件)
			break

		used[now] = True  # 頂点 now を X に追加
		res += mincost[now]  # 辺のコストを加える

		# 今回追加した頂点からのコストをmincostに加味する(次のループへの準備)
		for i in range(V):
			mincost[i] = min(mincost[i], cost[now][i])

	return res
