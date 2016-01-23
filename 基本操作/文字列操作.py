a + b         # a と b を連結します(not destructive)
a * n         # n 回繰り返します
a[n]          # n 番目の文字を取り出します
a[n:m]        # n 番目から m 番目までの文字列を取り出します
a[n:]         # n 番目から最後までの文字列を取り出します
a[:m]         # 0 番目から m 番目までの文字列を取り出します
a[n:m:s]      # n 番目から m 番目までの文字列を s個とばしで取り出します

a[::-1]       # reverse (a[n:m:s]の亜種)

# 書き換え
StringOverwrite.py使う

# 型変換
ord   # char => ascii number
chr   # ascii number => char
"".join(char_list)   # char_listをstringに変換

# split
"he ll o".split(" ")

# equals
==
# isSubstring
a in b   # if a is substring of b, return True

