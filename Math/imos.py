# imos
# n は使用する区間
imos = [0] * (n+2)

for i in range(n):
    imos[l[i]] += 1
    imos[r[i]+1] -= 1

for i in range(n):
    imos[i+1] += imos[i]
