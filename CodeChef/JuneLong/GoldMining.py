T = int(input())
for _ in range(T):
	n = int(input())
	ga = gb = 0 
	for _ in range(n):
		G,a,b = map(int,input().split())
		if a == b:
			ga += (G/2)
			gb += (G/2)
		else:
			ratio = G/(a+b)
			ga += (ratio*b)
			gb += (ratio*a)
	print("{:.5f} {:.5f}".format(ga,gb))		
	