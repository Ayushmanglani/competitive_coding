T = int(input())
for _ in range(T):
	n,x = map(int, input().split())
	a = list(map(int, input().split()))
	a.sort()
	k = 0
	for i in range(n):		
		if a[i]>=(x+1)/2:
			break
		k+=1
	if a[-1] <= x:
		print(n)
	else:
		for j in range(i,n):
			while x < a[j]:
				k += 1
				x *= 2
			if x >= a[j]:
				k += 1
				x = a[j]*2
		print(k)