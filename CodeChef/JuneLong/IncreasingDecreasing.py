from collections import Counter
def find(A,N):
	B1 = []
	B2 = []
	m = max(A)
	k = 0
	count = (Counter(A))
	for i in count:
		if i == m:
			if count[i]>1:
				return()
		elif count[i] >2:
			return()
		elif count[i] == 2:
			B1.append(i)
			B2.append(i)		
		else:
			B1.append(i)

	B1.sort()
	B2.sort()		
	x =	[m]	
	res = B1 + x + B2[::-1]
	return(res) 
T = int(input())
for _ in range(T):
	N = int(input())
	A = list(map(int,input().split()))
	res = find(A,N)
	if res:
		print('YES')
		result = ''
		for i in res:
			result += str(i) + " "
		print(result)
	else:
		print('NO')
