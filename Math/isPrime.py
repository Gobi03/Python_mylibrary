def isPrime(n):
    if n == 1:
        return False
    else:
        i = 2
        while(i*i <= n):
            if n % i == 0:
                return False
            i += 1
        return True
