class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        c = 0
        for i in range(len(s)):
            for j in range(k,len(t)):
                if(s[i] == t[j]):
                    k = j +1
                    c = c + 1
                    break
        if c == len(s):
            return (True)
        else:
            return (False)