class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we can sort them and check if both s and t are same
        s_sort = sorted(s)
        t_sort = sorted(t)

        return True if s_sort==t_sort else False