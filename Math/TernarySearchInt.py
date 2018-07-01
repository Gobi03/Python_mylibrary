# check は数値を返す

# 上に凸のグラフの最大値
def ternarySearchInt(small, big):
    def func(small, big):
        if big - small == 2:  # 終了条件
            mid = (big + small) // 2
            if check(big) >= check(mid):
                return big
            else:
                return small if check(small) >= check(mid) else mid
        else:
            midl = (big + small) // 2
            midr = midl + 1
            if check(midl) <= check(midr):
                return func(midl, big)
            else:
                return func(small, midr)
    return func(small, big)


# 下に凸のグラフの最小値
def ternarySearchInt(small, big):
    if big - small <= 2:  # 終了条件
        mid = (big + small) // 2
        if check(big) <= check(mid):
            return big
        else:
            return small if check(small) <= check(mid) else mid
    else:
        midl = (big + small) // 2
        midr = midl + 1
        if check(midl) >= check(midr):
            return ternarySearchInt(midl, big)
        else:
            return ternarySearchInt(small, midr)
