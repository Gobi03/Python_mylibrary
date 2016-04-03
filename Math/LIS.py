# 要テスト

# O(n log(n))
# A が LIS 抜き出すの長さ求めるリスト

A = [2,3,1,4]  # original sequence

## binary search
# 条件を満たす最小の値を返す
def binarySearch(l, r, ins, L):
	mid = (l + r) // 2
	if r == l or r == l + 1:
		if ins < L[l]:
			return l
		else:
			return r
	else:
		if ins < L[mid]:
			return binarySearch(l, mid, ins, L)
		else:
			return binarySearch(mid, r, ins, L)


## LISを返す(retrun int list)
def LIS():
	Lans = [A[0]] # 完成した LIS が入る
	L = [A[0]]    # 計算用
	length = 1

	for i in range(1, len(A)):
		if A[i] >= L[length-1]:  # 要素の追加
			L.append(A[i])
			Lans.append(A[i])
			length += 1
		else:    # 要素の更新
			ind = binarySearch(0, length - 1, A[i], L)
			L[ind] = A[i]
			if ind == length - 1:  # 末尾書き換えたら Lans 更新
				Lans = L[:]

	return Lans
