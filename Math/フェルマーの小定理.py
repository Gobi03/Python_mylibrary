# 要テスト

# mod m における a の逆元 つまり  ax ≡ 1 (mod m) を満たす x を求める
# m が素数かつ、a と m が互いに素である必要がある
# O(log(N))
## a^m ≡ a (mod m) -> a^(m-2) ≡ a^(-1) (mod m) -> a^(-1) ≡ a^(m-2) (mod m)

def fermatLT(a, m):
    MOD = m
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

    return repeatSquares(a, m-2) % m

print(fermatLT(7,29))
