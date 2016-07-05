# mod m における a の逆元 つまり  ax ≡ 1 (mod m) を満たす x を求める
# m が素数かつ、a と m が互いに素の場合はフェルマーの小定理のほうが高速に解ける
# O(N) -> O(log(N))

def mod_inverse(a, m):
	def gcdExt(a, b): # a >= b
		if b == 0:
			return (1, 0)
		else:
			q = a // b
			(px, py) = gcdExt(b, a % b)
			x = py
			y = px - q * py
			return (x, y)

	##
	(x, y) = gcdExt(a, b)
	return (m + (x % m)) % m
