# O(log min(a, b))
# 最大公約数
# ユークリッドの互除法
def gcd(a, b):  # a >= b
	if b == 0:
		return a
	else:
		return gcd(b, a % b)
