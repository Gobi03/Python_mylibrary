import math

N = 10000   # N is max number
prime = [True]*(N+1)
prime[0] = False
prime[1] = False

R = int(math.sqrt(N))

for i in range(2, R+1):
    if prime[i]:
        cnt = 2
        while i * cnt <= N:
            prime[i * cnt] = False
            cnt += 1

            
# if prime[i] = True, i is prime number
