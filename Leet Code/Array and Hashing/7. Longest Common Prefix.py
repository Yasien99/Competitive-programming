class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        for i in range(len(strs[0])):
            for st in strs[1:]:
                if i == len(st) or st[i] != strs[0][i]:
                    return out
            out = out + strs[0][i]  
                
        return out