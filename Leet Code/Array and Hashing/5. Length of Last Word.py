class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.strip()
        sum = 0
        for i in range(len(st)-1, -1, -1):
            if st[i] == " ":
                 break
            else:
                sum = sum +1
        return sum