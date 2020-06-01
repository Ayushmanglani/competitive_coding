n = int(input())
m = n
k = 0
while n>0:
    k += 1
    n = n//10
# print(k)
d = 10 ** (k-1)
if m%d in [2,3,7,8]:
	print(False)
else:
	s = 0
	while m>0:
		s += m%10
		m = m//10
	k = 0
	while s>10:
		k += s%10
		s = s//10
	# print(k,s)
	if k+s>=10:
		k = (k+s)%10
	if k+1 in [1,4,7,9]:
		print(True)
	else:
		print(False)