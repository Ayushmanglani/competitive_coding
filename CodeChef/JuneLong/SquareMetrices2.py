T = int(input())
for _ in range(T):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	b = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			b[i][j] = a[i]+a[j]
	count = 0
	for k in range(2,n):
		for i in range(n-k+1):
			for j in range(n-k+1):
				s = 0
				for l in range(i,i+k):
					s += sum(b[l][j:j+k])					
				if s == x:
					count += 1		
	print(count)
	