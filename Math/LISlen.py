# O(n log(n))
# 順序は <
# A が LIS 抜き出すの長さ求めるリスト

A = [2,3,1,4]  # original sequence

## binary search
# 条件を満たす最小の値を返す
def binarySearch(l, r, now, L):
    mid = (l + r) // 2
    if r == l or r == l + 1:
        if now <= L[l]:
            return l
        else:
            return r
    else:
        if now <= L[mid]:
            return binarySearch(l, mid, now, L)
        else:
            return binarySearch(mid, r, now, L)


## LISlen
def LISlen():
    L = []
    L.append(A[0])
    length = 1

    for i in range(1, len(A)):
        if A[i] > L[length-1]:  # 末端の要素より大きかったら
            L.append(A[i])
            length += 1
        else:  # 自分以上の数値の中で、一番小さいものと置換
            ind = binarySearch(0, length - 1, A[i], L)
            L[ind] = A[i]
    return length
