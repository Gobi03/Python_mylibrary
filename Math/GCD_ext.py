# 拡張ユークリッドの互除法
# ax + by = gcd(x, y) となる a, b の１つを求めることができる。

## x, y をグローバルっぽい感じに取りたい？実装できてるか微妙
# reference: チーター本 P.416

def extgcd(a, b, x, y): # a,b: Int, x,y: List[Int]
	g = a
	x[0] = 1
	y[0] = 0

	if b != 0:
		g = extgcd(b, a%b, y, x)
		y[0] -= (a / b) * x[0]

	return g
