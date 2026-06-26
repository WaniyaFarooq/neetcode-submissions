class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = "".join(ch for ch in s if ch.isalnum())

        
        print(s)
        p1 = len(s)-1
        p0 = 0

        while(p1 > p0):
            if s[p1] == s[p0]:
                p0=p0+1
                p1=p1-1
            else : return False

        return True

        
        