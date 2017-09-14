# 要テスト

# check は数値を返す

# 上に凸のグラフの最大値
def ternarySearchInt(small, big):
    # 初期条件
    if small == big:
        return small
    elif big - small == 1:
        if check(small) >= check(big):
            return small
        else:
            return big
    
    def func(small, big):
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
                return func(midl, big)
            else:
                return func(small, midr)
    return func(small, big)


# 下に凸のグラフの最小値
def ternarySearchInt(small, big):
    # 初期条件
    if small == big:
        return small
    elif big - small == 1:
        if check(small) <= check(big):
            return small
        else:
            return big

    def func(small, big):
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
                return func(midl, big)
            else:
                return func(small, midr)
    return func(small, big)
