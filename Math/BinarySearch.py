# 最大値を返す
def binarySearch(small, big):
	mid = (big + small) // 2
	if big == small or big == small + 1:
		if isWell(big):
			return big
		else:
			return small
	else:
		if isWell(mid):
			return binarySearch(mid, big)
		else:
			return binarySearch(small, mid)

# 最小値を返す
def binarySearch(small, big):
	mid = (big + small) // 2
	if big == small or big == small + 1:
		if isWell(small):
			return small
		else:
			return big
	else:
		if isWell(mid):
			return binarySearch(small, mid)
		else:
			return binarySearch(mid, big)
