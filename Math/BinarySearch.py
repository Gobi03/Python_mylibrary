# 条件を満たす最大の値を返す
def binarySearch(small, big):
    mid = (big + small) // 2
    if big - small <= 1:
        if check(big): return big
        else:          return small
    else:
        if check(mid):
            return binarySearch(mid, big)
        else:
            return binarySearch(small, mid)

# 条件を満たす最小の値を返す
def binarySearch(small, big):
    mid = (big + small) // 2
    if big - small <= 1:
        if check(small): return small
        else:            return big
    else:
        if check(mid):
            return binarySearch(small, mid)
        else:
            return binarySearch(mid, big)
