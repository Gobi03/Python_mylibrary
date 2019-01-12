## 最長共通部分列
# 文字列 s と t の共通部分文字列の長さの最大値を返す。

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

    return dp[len(s)][len(t)]
