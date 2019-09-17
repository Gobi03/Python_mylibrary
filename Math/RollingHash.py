# a は bに含まれているか
def contain(a, b):
    B = 10**9 + 7
    h = 1 << 64
​
    al = len(a); bl = len(b)
    if al > bl:
        return False
​
    # B の al 乗を計算
    t = 1
    for _ in range(al):
        t *= B
        t %= h
​
    # aとbの最初のal文字に関するハッシュ値を計算
    ah = 0; bh = 0
    for i in range(al):
        ah = (ah * B + ord(a[i])) % h
    for i in range(al):
        bh = (bh * B + ord(b[i])) % h
​
    # bの場所を1つずつ進めながらハッシュ値をチェック
    for i in range(bl-al + 1):
        if ah == bh:
            return True
        if i + al < bl:
            bh = (bh * B + ord(b[i + al]) - ord(b[i]) * t) % h
    
    return False
