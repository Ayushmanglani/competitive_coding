T = int(input())
for _ in range(T):
	S,N = map(int,input().split())
	if S<=N:
		if S>1 and S%2 != 0:
			print(2)
		else:
			print(1)
	else:
		c = 0
		while S>N:
			c += S//N
			S = S%N
		if S>0:
			if S>1 and S%2 != 0:
				c += 2	 
			else:
				c += 1
		print(c)
'''
In a country called Chef Land, there was a lot of monetary fraud, so Chefu, the head of the country, decided to choose new denominations of the local currency ― all even-valued coins up to an integer N should exist. After a few days, a citizen complained that there was no way to create an odd value, so Chefu decided that he should also introduce coins with value 1. Formally, you are given an integer N; for v=1 and each even positive integer v≤N, coins with value v exist.

You are also given an integer S. To handle transactions quickly, find the minimum number of coins needed to pay a price S.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers S and N.
Output
For each test case, print a single line containing one integer ― the minimum number of coins.

Constraints
1≤T≤10,000
1≤S≤109
2≤N≤109
N is even
Subtasks
Subtask #1 (100 points): original constraints

Example Input
4
2 2
1 14
30 10
31 4
Example Output
1
1
3
9