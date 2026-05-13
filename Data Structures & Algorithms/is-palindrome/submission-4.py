class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.replace("?","")
        s = s.replace(",", "")
        s = s.replace(".", "")
        s= s.replace("'","")
        s = s.replace(":","")
        s = s.lower()
        s_copy = ""
        i = len(s)-1
        while i>=0:
            s_copy += s[i]
            i -=1
        if s == s_copy:
            return True
        else:
            return False
        
