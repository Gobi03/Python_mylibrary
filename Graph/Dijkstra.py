# O(E log(V))
import heapq

edge = [0]*v  # 頂点 i から行くことができる頂点のリスト
dist = makelist(a, b)  # 頂点 a から頂点 b に移動するコスト

for i in range(v):
	edge[i] = []

# fro から to への最短距離(v は頂点数)
def dijkstra(fro, to, v):
	MAX = int(1e9)

	d = [MAX]*v   # fro からの距離を格納する
	check = [False]*v  # すでにその頂点からを調べたかのフラグ

	d[fro] = 0
	pq = [(0, fro)]    # priority queue: (cost, node) queue


	# 頂点は v 個あるので、v 周する
	for i in range(v):
		# 調べ済みでない頂点のうち、最も近い頂点を now に入れる
		now = -1        # このターンにフォーカスするノード
		nowdis = MAX    # その距離

		while True:
			now = heapq.heappop(pq)[1]  # 最小コストから貪欲に取っていく
			if not check[now]:    # まだチェックされていないノードだったら決定
				check[now] = True
				nowdis = d[now]
				break

		# その頂点からたどり着ける頂点の情報を更新する
		for nex in edge[now]:  # nex はたどり着ける頂点
			nexdis = d[now] + dist[now][nex]
			if nexdis < d[nex]:  # 既存の通路より近いなら更新
				d[nex] = nexdis
				heapq.heappush(pq, (d[nex], nex))

	return d[to]
