## セット(set)
a = set(['red', 'blue', 'green'])
b = set(['green', 'yellow', 'white'])

# 要素の追加
a.add(['black'])

# 差集合
print a - b            #=> set(['red', 'blue'])
# 和集合
print a | b            #=> set(['red', 'blue', 'green', 'yellow', 'white'])
# 積集合
print a & b            #=> set(['green'])
# XOR
print a ^ b            #=> set(['red', 'blue', 'yellow', 'white'])

# 要素が含まれているかどうか
print 'green' in a     #=> True


