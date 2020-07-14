T = int(input())
for _ in range(T):
	n = int(input())
	pa = pb = 0
	for _ in range(n):
		a,b = map(int, input().split())
		sa = 0
		while a>0:
			sa += (a%10)
			a = a//10
		sb = 0
		while b>0:
			sb += (b%10)
			b = b//10
		if sa > sb:
			pa += 1
		elif sb > sa:
			pb += 1
		else:
			pa += 1
			pb += 1
	if pa>pb:
		print(0,pa)
	elif pb>pa:
		print(1,pb)
	else:
		print(2,pb)