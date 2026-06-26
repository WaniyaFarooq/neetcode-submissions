class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 : return 0
        nums = sorted(set(nums))
        
        ans = 1
        longest =1
        for index in range(1,len(nums)):
            if nums[index]==(nums[index-1])+1:
                ans+=1
            else: ans=1

            longest = max(ans,longest)
            
        return longest

        