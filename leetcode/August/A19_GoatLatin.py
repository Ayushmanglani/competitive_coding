class Solution:
    def toGoatLatin(self, S: str) -> str:
        s = S.split()
        vowel = {'a','e','i','o','u'}
        res =""
        for k,i in enumerate(s):
            if len(i) == 1 or i[0].lower() in vowel:
                res += i + "ma" + "a"*(k+1) + " "
            else:
                res += i[1:] + i[0] + "ma" + "a"*(k+1) + " "
            k += 1
        return(res.strip())