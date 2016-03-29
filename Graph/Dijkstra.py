edge = [[]]*v  # 頂点 i から行くことができる頂点のリスト
dist = makelist(a, b)  # 頂点 a から頂点 b に移動するコスト

# fro から to への最短距離(v は頂点数)
def dijkstra(fro, to, v):
	MAX = int(1e9)
	d = [MAX]*v   # fro からの距離を格納する
	dp = [False]*v  # すでにその頂点からを調べたかのフラグ

	d[fro] = 0

	# 頂点は v 個あるので、v 周する
	for i in range(v):
		# 調べ済みでない頂点のうち、最も近い頂点を now に入れる
		now = -1
		nowdis = MAX
		for j in range(v):
			if nowdis > d[j] and not dp[now]:
				nowdis = d[j]   # 暫定の最小値
				now = j       # 暫定の次回スタート番号

		# もし調べ済みで到達可能な頂点がない場合は break する
		if nowd == MAX:
			break

		# 調べる頂点には必ずフラグを立てる
		check[now] = True
		# その頂点からたどり着ける頂点の情報を更新する
		for nex in edge[now]:
			nex = edge[now][j]
			nexdis = d[now] + dist[now]
			if nexdis < d[nex]:
				d[nex] = nexdis

	return d[to]
