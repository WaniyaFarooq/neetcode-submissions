class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for a in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(a) !=t.count(a):
                return False
        return True
            
        