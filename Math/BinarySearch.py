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
			binarySearch(mid, big)
		else:
			binarySearch(small, mid)

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
			binarySearch(small, mid)
		else:
			binarySearch(mid, big)
