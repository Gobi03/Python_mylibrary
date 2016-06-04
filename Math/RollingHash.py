MOD = int(1e9) + 7
BASE = 2837

# a は b に含まれているか O( max(al, bl-al) )
def contain(a, b):
	al = len(a)
	bl = len(b)
	
	if al > bl:
		return False

	# B の al乗を計算
	t = 1
	for i in range(al):
		t = (t * BASE) % MOD

	# a と b の最初の al 文字に関するハッシュ値を計算
	ah = 0
	bh = 0
	for i in range(al):
		ah = (ah * BASE + a[i]) % MOD
	for i in range(bl):
		bh = (bh * BASE + b[i]) % MOD

	# b の場所を１つずつ進めながらハッシュ値をチェック
	for i in range(bl - al + 1):
		if ah == bh:
			return True   # b の i 文字目からの al 文字が一致
		if i + al < bl:
			bh = (bh*B + b[i+al] - b[i]*t) % MOD  # i+1 文字目から al 文字をセット
			if bh < 0:       ## 要らないかも(チェックする)
				bh = MOD + bh
	return False
	

# a の末尾と b の先頭を何文字重ねることができるか
def overlap(a, b):
	al = len(a)
	bl = len(b)

	ans = 0
	
	ah = 0
	bh = 0
	t = 1
	for i in range(1, min(al, bl) + 1):
		ah = (ah + a[al-i] * t) % MOD    # a の末尾 i 文字のハッシュ値
		bh = (bh * BASE + b[i-1]) % MOD  # b の末尾 i 文字のハッシュ値
		if ah == bh:
			ans = i
		t *= B

	return ans
