class Solution(object):
    def decodeString(self, s):
        it, num, stack = 0, 0, [""]
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] == "[":
                stack.append(num)
                num = 0
                stack.append("")                
            elif s[it] == "]":
                str1 = stack.pop()
                rep = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1 * rep)
            else:
                stack[-1] += s[it]              
            it += 1           
        return "".join(stack)

class Solution:
    def decodeString(self, s):
        def recur(s):
            ans = '' #answer from this step of recursion
            i = 0 #index of input string s
            num = '' #repetition number if any character is repeated
            while i<len(s):
                x = s[i]
                if x.isnumeric(): #we get a digit, append it to num
                    num += x
                elif x=='[': #we are opening a bracket
                    #now find j and i such that s[j:i] is the string inside the bracket
                    bal = 1 
                    j = i+1
                    while bal:
                        i += 1
                        if s[i]=='[': bal += 1
                        if s[i]==']': bal -= 1
                    #we add num*s[j:i]
                    #but we apply the function recursively in case there is a nested bracket
                    ans += int(float(num))*recur(s[j:i]) 
                    num = '' #reset num
                else: #we get a regular character, just append it
                    ans += x
                i += 1 #increment counter
            return ans
        
        return recur(s)        