class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        already_smaller = 0
        same_so_far = True
        N = str(n)
        for c in N:
            already_smaller *= len(digits)
            ct_smaller_digits = len([d for d in digits if d < c])
            if same_so_far:
                already_smaller += ct_smaller_digits
                same_so_far = c in digits
            already_smaller += 1 # we could put blank
        
        return already_smaller + (1 if same_so_far else 0) - 1

class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in xrange(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]
        # print(dp)
        # print(len(D)) #'4 + 8 + 16'
        return dp[0] + sum(len(D) ** i for i in xrange(1, K))        