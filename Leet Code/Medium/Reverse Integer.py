class Solution:
    MIN_INT = -2147483648
    MAX_INT = 2147483647
    def reverse(self, x: int) -> int:
        if(x == 0):
            return 0
        S = str(x)
        j = len(S) - 1
        while(S[j] == '0'):
            ListS = list(S)
            ListS.pop(j)
            S = "".join(ListS)            
            j = j - 1
        if(S[0] == '-'):
            S = S[j:0:-1]
            if int(S) not in range(self.MIN_INT, self.MAX_INT) : return 0
            else: return '-' + S
              
        else :
            S = S[::-1]
            if int(S) not in range(self.MIN_INT, self.MAX_INT) : return 0
            else: return S

