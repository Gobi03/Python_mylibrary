# ref: http://www.slideshare.net/iwiwi?utm_campaign=profiletracking&utm_medium=sssite&utm_source=ssslideview  p.47
INT_MAX = 2147483647

# 要素数
N = 35

# ele は作るセグツリーの要素数(簡単のため２のべき乗とする)
ele = 1
while ele >= N:
	ele *= 2

## making a seg tree
seg = [INT_MAX]*(ele + ele - 1)
# input
init = ele - 1
for i in range(init, init + N):
	seg[i] = int(input())

# fill in its nodes
nowele = ele // 2
while start >= 1:
	for i in range(nowele-1, (nowele-1)+nowele):
		seg[i] = min(seg[i*2 + 1], seg[i*2 + 2])
	nowele = nowele // 2

### complete making a RMS

## query function
# 区間[a, b)の最小値を求めるクエリ(include a, not include b)
# O(log(N))
# using as query(a, b, 0, 0, ele)
def query(a, b, k, l, r):
	# [a, b)に[l, r)が含まれない
	if r <= a or l >= b:
		return INT_MAX

	# [a, b)が[l, r)を完全に含むか
	if (a <= l and b >= r):
		return seg[k]
	else:
		vl = query(a, b, k*2+1, l,        (l+r)//2)
		vr = query(a, b, k*2+2, (l+r)//2, r       )
		return min(vl, vr)
