import random

random.randint(x,y)  # x～yまでのint値を取得します。

random.uniform(x,y)  # x～yまでのfloat値を取得します。

random.choice(param)  # param内から一つの要素を取得します。

random.shuffle(array)  # array内の要素をシャッフルします。

def randStr(n):
    res = ""
    for _ in range(n):
        res += chr(random.randint(ord('a'), ord('z') + 1))
