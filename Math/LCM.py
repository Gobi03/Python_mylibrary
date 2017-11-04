# 最小公倍数
# ユークリッドの互除法
def lcm(a, b): 
    def gcd(a, b):  # a >= b
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    return a * b // gcd(a, b)
