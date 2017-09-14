## 最長共通部分列
# 文字列 s と t の共通部分文字列の長さの最大値を返す。

def makelist(n, m):
    return [[0 for i in range(m)] for j in range(n)]

# str * str -> int
def solve(s, t):
    # 何文字目かで index (offset=1)
    dp = makelist(len(s)+1, len(t)+1)
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[len(s)][len(t)]
