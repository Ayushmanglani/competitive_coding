class Solution(object):
    def decodeAtIndex(self, S, K):
        stack, l = [], 0
        for c in S:
            l = l + 1 if c.isalpha() else l * int(c)
            stack += c,
            while l >= K:
                while stack[-1].isdigit(): 
                    l //= int(stack.pop())
                K = K % l
                if not K: 
                    return stack[-1]
                l -= 1
                stack.pop()

class Solution(object):
    def decodeAtIndex(self, S, K):
        size = 0
        for c in S:
            if c.isalpha():
                size += 1
            else:
                size *= int(c)
        
        for i in range(len(S)-1,-1,-1):
            K = K % size
            if K == 0 and S[i].isalpha():
                return S[i]
            
            if S[i].isalpha():
                size -= 1
            else:
                size /= int(S[i])                