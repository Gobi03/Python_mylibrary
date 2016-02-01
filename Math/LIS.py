# LISを返す(retrun int list)
def LIS():
	Llist = [].append([A[0]]) # length = 1から順に詰めてく
	L = [].append(A[0])
	length = 1
		
	for i in range(1, len(A)):
		if L[length-1] <= A[i]:
			L.append(A[i])
			a = []
			for e in L:
				a.append(e)
			Llist.append(a)
			length += 1
		else:
			for k in range(length):
				if(L[k] > A[i]):
					L[k] = A[i]
					break
	return Llist[-1]
