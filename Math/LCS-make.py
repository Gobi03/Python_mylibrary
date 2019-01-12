# 文字列 s と t の最長共通部分列を作って返す

def makelist(n, m):
    return [[0 for i in range(m)] for j in range(n)]

# str * str -> int
def solve(s, t):
    dp = makelist(len(s)+1, len(t)+1) # 何文字目かで index (offset=1)
    
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    res = ""
    x, y = len(t), len(s)
    
    while dp[y][x] > 0:
        now = dp[y][x]
        u, lu, l = dp[y-1][x], dp[y-1][x-1], dp[y][x-1]
        if lu == now:
            x -= 1
            y -= 1
        else: # lu = now - 1
            if u == lu and l == lu:
                res += s[x-1]
            else:
                if u >= l:
                    y -= 1
                else:
                    x -= 1
                    
    return res[::-1]
