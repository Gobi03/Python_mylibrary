# reference: http://pekempey.hatenablog.com/entry/2015/12/09/000603

def makelist(n, m, o):
	return [[[0 for i in range(o)] for j in range(m)] for k in range(n)]

def f(s):
	MOD = int(1e9+7)
	dp = makelist(142, 2, 2)  # 0: 制限入る, 1: 0~9までOK
	n = len(s)

	dp[0][0][0] = 1
	# i: 上からi桁目まで見ている
	# j: s 未満であることが確定している
	# k: すでに 4 を選んでいる 
	for i in range(n):
		for j in range(2):  # j==1, k==1 の操作は単なる移植
			for k in range(2):
				# j==0: focus してる桁の数字
				# j==1: 9 (全桁)
				lim = (9 if j==1 else int(s[i])-int('0'))

				for d in range(lim + 1):  # (0 to digit) or (0 to 9)
					dp[i+1][j or d<lim][k or d==4 or d==9] += dp[i][j][k]

	res = 0
	for j in range(2):
		res += dp[n][j][1]
		res %= MOD
	return res
