class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            a =d.get(i,0)
            a=a+1;
            if a>1: return True
            d[i] =a;
        return False
        