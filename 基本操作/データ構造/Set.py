## セット(set)
a = set()

b = set(['red', 'blue', 'green'])
c = set(['green', 'yellow', 'white'])

# 要素の追加
a.add('black')

## 集合演算
print a - b   # 差集合
print a | b   # 和集合
print a & b   # 積集合
print a ^ b   # XOR

# 要素が含まれているかどうか
print 'green' in a     #=> True


