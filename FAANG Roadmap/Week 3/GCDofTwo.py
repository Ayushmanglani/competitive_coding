for _ in range(int(input())):
    a,b = map(int, input().split())
    def gcd(a,b): 
        if (a == 0): 
            return b 
        if (b == 0): 
            return a 
        if (a == b): 
            return a 
        if (a > b): 
            return gcd(a-b, b) 
        return gcd(a, b-a)
    print(gcd(a,b))

for _ in range(int(input())):
    a,b = map(int, input().split())
    def gcd(a,b): 
        if (b == 0): 
             return a 
        return gcd(b, a%b) 
    print(gcd(a,b))