class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col_del = 0 
        for i in range (len(strs[0])):
            curr_alpha = ord(strs[0][i])
            for j in range (1, len(strs)):
                if ord(strs[j][i]) >= curr_alpha:
                    curr_alpha = ord(strs[j][i])
                else:
                    col_del += 1
                    break
        return col_del

