# cons
[1, 2, 3].append(4)         # destructive
# append
[1, 2, 3].extend([4, 5, 6])   # destructive
[1, 2, 3] + [4, 5, 6]        # destructive

# length
len([1, 2, 3])           #=> 3
# map
a = [1, 2, 3]
a.map(lambda x: x * 2, a)    # destructive
[map(lambda x: x * 2, a)]       # not destructive
[x * 2 for x in a]            #=> [2, 4, 6] : 内包表記
# filter
a = [1, 2, 3]
print filter(lambda x: x % 2, a)
print [x for x in a if x % 2]       #=> [1, 3] : 内包表記

# reduce() はリストの最初の2要素を引数に処理を呼び出し、結果と次の要素を引数に処理の呼び出しを繰り返し、単一の結果を返します。下記の例では、各要素の合計を計算しています。
a = [1, 2, 3, 4, 5]
print reduce(lambda x, y: x + y, a) #=> 15 : lambda方式
# pop (destructive)
elm = a.pop()              # リストの末尾から要素を1つ取り出す
elm = a.pop(0)             # 引数にリストのインデックスを取り、その要素を取り出す
                           # => a = [2,3,4,5]   elm = 1
# put
[1, 2, 4].insert(2, 3)     # => [1, 2, 3, 4]
# remove
a.remove(13)               # 引数のオブジェクトのうちリストの先頭に最も近いもの一つだけ削除する   [13, 5, 13].remove(13) => [5, 13]

# sort
a.sort()   # destructive
sorted(a)  # not destructive

# 要素 e が含まれているかどうか
e in listname   # => True or False
e not in listname  # 含まれていないとTrue
