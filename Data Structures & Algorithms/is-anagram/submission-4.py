class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hm = {}
        t_hm = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_hm[s[i]] = s_hm.get(s[i], 0) + 1
            t_hm[t[i]] = t_hm.get(t[i], 0) + 1

        return s_hm == t_hm
        