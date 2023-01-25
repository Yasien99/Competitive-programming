class Solution:
    def removeNonAlpha (self, s: str):
        alphaS = ""
        for st in s:
            if st.isalpha():
                alphaS += st.lower()
            if st.isnumeric():
                alphaS += st
        print(alphaS)
        return alphaS

    def isPalindrome(self, s: str) -> bool:
        newS = self.removeNonAlpha(s)
        sLen = len(newS)
        i = 0 
        j = sLen - 1
        while (i < sLen/2):
            if newS[i] != newS[j]:
                return False
            else:
                i += 1
                j -= 1        
        return True
        

