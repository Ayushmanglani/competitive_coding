T = int(input())
for _ in range(T):
	n = int(input())
	a = list(map(int, input().split()))
	c = 0
	for i in range(n-1):
		p = abs(a[i]-a[i+1])-1
		if p > 0:
			c += p
	print(c)