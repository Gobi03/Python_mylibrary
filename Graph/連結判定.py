import queue

edge = makelis(a, b)  # 頂点 a の b 番目の辺が edge[a][b] に入る

# from から to につながっているかどうかを判定する関数。頂点数は v
def isConnect(fro, to, v):
	dp = [False]*v
	q = queue.Queue()
	q.put(fro)
	dp[fro] = True
	
	# BFSの基本的な構文
	while not q.empty():
		now = q.get()
		for nex in edge[now]:
			if nex == to:  # 目的の頂点にたどり着いたらTrueを返す。
				return True
			elif dp[nex]:  # 検査済みなら打ち切り
				continue
			
			dp[nex] = True
			q.put(nex)
	return False
