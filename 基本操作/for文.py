for i in range(10):     # 処理を10回繰り返す(i = 0 ~ 9)

for k in {'one': 1, 'two': 2, 'three': 3}:
  print k                  #=> one, two, three
for c in "123":
  print c                  #=> 1, 2, 3
for line in open("sample.txt"):
  print line               # 1行ずつ表示


# else がある場合は、ループの最後に else節を実行します。
for n in [1, 2, 3]:
    print n
else:
    print 'END'

# enumerate
list1 = ['a', 'b', 'c']
for (i, x) in enumerate(list1):
	print i,x
0 a
1 b
2 c
