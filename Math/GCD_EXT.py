# 拡張ユークリッドの互除法
# ax + by = gcd(a, b) となる x, y の１つを求めることができる。
### まだコード追えてない

def gcdExt(a, b): # a >= b
	if b == 0:
		return (1, 0)
	else:
		q = a // b
		(px, py) = gcdExt(b, a % b)
		x = py
		y = px - q * py
		return (x, y)

print(gcdExt(13, 5))
