class Solution:
    def list_maker(self, s:str) -> str:
        sort_list = []
        for i in range(len(s)):
            sort_list.append(s[i])
        return sort_list
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = self.list_maker(s)
        sort_t = self.list_maker(t)
        sort_s.sort()
        sort_t.sort()
        if len(sort_s)!=len(sort_t):
            return False
        else:
            for i in range(len(sort_s)):
                if (sort_s[i]==sort_t[i]):
                    continue
                else:
                    return False
                
        return True
        