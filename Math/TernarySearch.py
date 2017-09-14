# 上に凸のグラフの最大値
def ternarySearch(small, big):
    END = 5e-9
    VOL = 1e-9  # END // 2 より小さい
    def func(small, big):
        midl = (big + small) / 2
        midr = midl + VOL
        if big - small < END:  # 終了条件
            return big
        else:
            if check(midl) <= check(midr):
                return func(midl, big)
            else:
                return func(small, midr)

    return func(small, big)


# 下に凸のグラフの最小値
def ternarySearch(small, big):
    END = 5e-9
    VOL = 1e-9  # END // 2 より小さく
    def func(small, big):
        midl = (big + small) / 2
        midr = midl + VOL
        if big - small < END:  # 終了条件
            return big
        else:
            if check(midl) >= check(midr):
                return func(midl, big)
            else:
                return func(small, midr)

    return func(small, big)
