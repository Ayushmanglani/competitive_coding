def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m
        m = a % m 
        a = t 
        t = y 
        y = x - q * y 
        x = t  
    if (x < 0) : 
        x = x + m0 
    return x

def pfx(s):
    p=[]
    for i in range(len(s)):
        p.append("".join(s[:i+1]))
    return p
def wgt(s,d):
    k=list(s)
    ans=0
    for i in k:
        ans+=d[i]
    return ans
def sub(s):
    k=list(s)
    ans=[]
    for i in range(len(k)):
        for j in range(i,len(k)):
            ans.append("".join(k[i:j+1]))
    return ans
        
for tt in range(int(input())):
    st=list(input())
    s1="".join(st)
    w=list(map(int,input().split()))
    d={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    k=0
    for i in d:
        d[i]=w[k]
        k+=1
    subs=sub(st)
    d1={}
    for i in subs:
        d1[i]=0
    for i in subs:
        d1[i]+=1
    def choose(s):
        p=pfx(s)
        a=[]
        for i in p:
            num=len(s)//len(i)
            n1=len(s)%len(i)
            flg=0
            chk=""
            num1=num
            while(num1):
                chk+=i
                if(s.find(chk)==-1):
                    flg=1
                    break
                num1-=1
            if(flg!=1):

                fg=0
                if(n1!=0):
                    l=num*len(i)
                    r="".join(s[l:])                    
                    if(i.find(r)!=0):
                        fg=1
                    else:
                        a.append(i)
                else:
                    a.append(i)
            else:
                continue
        return a
    
    ws={}
    for i in d1:
        ans=wgt(i,d)
        ws[i]=ans
    ps={}
    for i in d1:
        x=choose(i)
        q=0
        for i in x:
            q+=ws[i]
        ps[i]=q
    ans=0
    for i in ps:
        ans+=(d1[i]*ps[i])
    total=(len(s1)*(len(s1)+1))//2
    print(ans*modInverse(total,998244353)%998244353)