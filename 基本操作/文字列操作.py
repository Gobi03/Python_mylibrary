a + b         # a と b を連結する(not destructive)
a * n         # n 回繰り返す
a[n:m]        # n から m-1 番目までの文字列を取り出す
a[n:]         # n 番目から最後までの文字列を取り出す
a[:m]         # 0 から m-1 番目までの文字列を取り出す
a[n:m:s]      # n 番目から m 番目までの文字列を s個飛ばしで取り出す

a[::-1]       # reverse (a[n:m:s]の亜種)

# 書き換え
StringOverwrite.py (mylibrary) 使う

# 型変換
ord   # char => ascii number
chr   # ascii number => char
"".join(char_list)   # char_listをstringに変換

# 大文字小文字変換
文字列.upper()  # 大文字に
文字列.lower()  # 小文字に

# split
"he ll o".split(" ")
split(",")  # 引数でsplit

# equals
==

# isSubstring
a in b   # if a is substring of b, return True
