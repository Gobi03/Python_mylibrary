#  pas = pascal(n)
#  nCk = pas(k)
#  n = 0 に対応していない

MOD = int(1e9) + 7

def makePascal(n):  # l[m][k] で mCk を取り出せるリストを返す
    res = [[1]]

    for m in range(1, n+1):
        l = []
        for k in range(m + 1):
            if k == 0 or k == m:
                l.append(1)
            else:
                tmp = res[m-1][k-1] + res[m-1][k]
                tmp %= MOD  # MOD要らないなら消す
                l.append(tmp)
        res.append(l)

    return res
