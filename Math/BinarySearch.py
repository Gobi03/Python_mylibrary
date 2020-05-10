# 条件を満たす最大の値を返す
def binarySearch(_small, _big):
    def check(i):
        return True

    def func(small, big):
        mid = (big + small) // 2
        if big - small <= 1:
            if check(big): return big
            else:          return small
        else:
            if check(mid):
                return func(mid, big)
            else:
                return func(small, mid)

    return func(_small, _big)


# 条件を満たす最小の値を返す
def binarySearch(_small, _big):
    def check(i):
        return True

    mid = (big + small) // 2
    if big - small <= 1:
        if check(small): return small
        else:            return big
    else:
        if check(mid):
            return func(small, mid)
        else:
            return func(mid, big)

    return func(_small, _big)
