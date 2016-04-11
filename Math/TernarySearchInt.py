# 要テスト

# 上に凸のグラフの最大値
def ternarySearchInt(small, big):
	midl = (big + small) // 2
	midr = midl + 1
	if big - small == 2:  # 終了条件
		mid = midl
		if check(small) >= check(mid):
			if check(small) >= check(big):
				return small
			else:
				return big
		else:
			if check(mid) >= check(big):
				return mid
			else:
				return big
	else:
		if check(midl) <= check(midr):
			return ternarySearchInt(midl, big)
		else:
			return ternarySearchInt(small, midr)


# 下に凸のグラフの最小値
def ternarySearchInt(small, big):
	midl = (big + small) // 2
	midr = midl + 1
	if big - small == 2:  # 終了条件
		mid = midl
		if check(small) <= check(mid):
			if check(small) <= check(big):
				return small
			else:
				return big
		else:
			if check(mid) <= check(big):
				return mid
			else:
				return big
	else:
		if check(midl) >= check(midr):
			return ternarySearchInt(midl, big)
		else:
			return ternarySearchInt(small, midr)
