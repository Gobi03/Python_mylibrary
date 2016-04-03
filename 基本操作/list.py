# initialize
l = [0] * 3     # l = [0, 0, 0]

# 値渡し
l2 = l[:]

# index
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a1 = a[2:4]     # 2番目から3番目: [2, 3]
a2 = a[2:]      # 2番目から最後: [2, 3, 4, 5, 6, 7, 8, 9]
a3 = a[:4]      # 最初から3番目: [0, 1, 2, 3]
a1 = a[1:8:2]   # 1番目から7番目まで2個とばし: [1, 3, 5, 7]
b1 = a[-1]      # マイナスの値を指定すると、後ろから数えます。: 9
b2 = a[-2]      # : 8


## リストの内包表記
a = [1, 2, 3]
print [x * 2 for x in a]                        #=> [2, 4, 6]
print [x * 2 for x in a if x == 3]              #=> [6]
print [[x, x * 2] for x in a]              #=> [[1, 2], [2, 4], [3, 6]]
print [(x, x * 2) for x in a]                   #=> [(1, 2), (2, 4), (3, 6)]

b = [4, 5, 6]
print [x * y for x in a for y in b]             #=> [4, 5, 6, 8, 10, 12, 12, 15, 18]
print [a[i] * b[i] for i in range(len(a))]      #=> [4, 10, 18]
