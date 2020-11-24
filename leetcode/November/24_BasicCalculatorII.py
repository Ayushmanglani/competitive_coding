class Solution:
    def calculate(self, s):
        # translation, modified, and works , 96% faster and 50% less space
        if not s :
            return 0
        s +=')'
        n = len(s)
        stack =[]
        cur_num = 0
        cur_oper = "+"
        i = 0
        operator = ['+']
        while i < n:
            # print i
            char = s[i]
            if char.isdigit():
                cur_num = cur_num*10 + ord(char) - ord('0')
            if char.isdigit() == False and (char != ' ' or i == n-1):
                if cur_oper == '-':
                    stack.append(-cur_num)
                elif cur_oper == '+':
                    stack.append(cur_num)
                elif cur_oper == '*':
                    stack.append(stack.pop()*cur_num)
                elif cur_oper == '/':
                    prev_op = stack.pop()
                    if prev_op == 0:
                        sign = 1
                    else:
                        sign =  abs(prev_op)/prev_op
                    stack.append(sign*(abs(prev_op)//cur_num))
                cur_oper = char
                cur_num = 0
            i += 1
    
        result = 0
        while stack:
            result += stack.pop()
        return result