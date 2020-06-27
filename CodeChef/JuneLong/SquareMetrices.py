T = int(input())
for _ in range(T):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	b = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			b[i][j] = a[i]+a[j]
	count = 0
	stripSum = [[None] * n for i in range(n)] 
	for k in range(n):
		for j in range(n):
			Sum = 0
			for i in range(k): 
				Sum += b[i][j]  
			stripSum[0][j] = Sum
			for i in range(1, n - k + 1): 
				Sum += (b[i + k - 1][j] - b[i - 1][j])  
				stripSum[i][j] = Sum
		for i in range(n - k + 1):
			Sum = 0
			for j in range(k): 
				Sum += stripSum[i][j]  
			if Sum == x:
				count += 1
			for j in range(1, n - k + 1): 
				Sum += (stripSum[i][j + k - 1] - stripSum[i][j - 1])  
				if Sum == x:
					count += 1
	print(count)