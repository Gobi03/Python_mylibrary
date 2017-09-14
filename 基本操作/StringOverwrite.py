# stringの書き換え
# s[index] = c
def overwriteStr(s, index, c):
    tmp = list(s)
    tmp[index] = c
    return "".join(tmp)
