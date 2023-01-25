class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split(" ")
        pat_occ = {}
        st_occ = {}
        p_pat = []
        s_pat = []       
        k = 1  
        c = 1
        if len(word) != len(pattern):
            return False
        for i in range(len(word)):
            if word[i] in st_occ:
                s_pat.append(st_occ[word[i]])
            if word[i] not in st_occ:
                c += 1
                st_occ[word[i]] = c
                s_pat.append(st_occ[word[i]])

        for i in range(len(pattern)):
            if pattern[i] in pat_occ:
                p_pat.append(pat_occ[pattern[i]])
                
            if pattern[i] not in pat_occ:
                k += 1
                pat_occ[pattern[i]] = k
                p_pat.append(pat_occ[pattern[i]])             
        for i in range(len(s_pat)):
            if s_pat[i] != p_pat[i]:
                return False
        return True


