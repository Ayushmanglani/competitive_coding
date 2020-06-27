T = int(input())
for _ in range(T):
	N,K = map(int,input().split())
	A = list(map(int,input().split()))
	m = max(A)
	res = 0
	ms = 0
	for i in range(1,m+1):
		if K == bin(i).count('1'):
			s = 0
			for j in range(N):
				s += (i & A[j])
		if ms < s:
			ms = s
			res = i
	print(res)