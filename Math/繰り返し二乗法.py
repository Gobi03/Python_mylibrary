# O(log(n))

MOD = 1000000007
def repeatSquares(x, n):  # x^n
  ans = 1
  while n != 0:
    if n % 2 == 1:
      ans *= x
      ans %= MOD
    x *= x
    n //= 2
    x %= MOD      # MOD演算ないなら消していい
  return ans
