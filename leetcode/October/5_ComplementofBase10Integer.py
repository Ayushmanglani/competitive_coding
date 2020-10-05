class Solution:
    def bitwiseComplement(self, N: int) -> int:
        NB = bin(N)[2:]
        New = ''
        for i in NB:
            if i == '1':
                New += '0'
            else:
                New += '1'
        return(int(New,2))