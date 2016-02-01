A = [2,3,1,4]  # original sequence

def LISlen():
	L = []
	L.append(A[0])
	length = 1
	Llist.append([A[0]])
	for i in range(1, len(A)):
		if L[length-1] <= A[i]:  # 末端の要素より大きかったら
			L.append(A[i])
			length += 1
		else:
			for k in range(length):
				if(L[k] > A[i]):
					L[k] = A[i]
					break
	return length
