# O(log(n))

MOD = 1000000007
def repeatSquares(x, n):  # x^n
	res = 1
	while n != 0:
		if n % 2 == 1:
			res *= x
			res %= MOD  # MOD演算ないなら消していい
		x *= x
		n //= 2
		x %= MOD      # MOD演算ないなら消していい
	return res
