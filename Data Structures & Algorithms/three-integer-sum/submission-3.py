class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        # -4,-1,-1,0,1,2
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: continue
            fixed = 0-nums[i]
            pointer1 = i+1
            pointer2 = len(nums)-1
            while(pointer2>pointer1):
                if nums[pointer1]+nums[pointer2] == fixed:        
                    ans.append([nums[pointer1],nums[pointer2],0-fixed]) 
                    while pointer2>pointer1 and nums[pointer1]==nums[pointer1+1]:
                        pointer1=pointer1+1
                    while pointer2>pointer1 and nums[pointer2]==nums[pointer2-1]:
                        pointer2=pointer2-1
                    pointer1=pointer1+1
                    pointer2=pointer2-1

    
                elif nums[pointer1]+nums[pointer2] > fixed:
                    pointer2=pointer2-1
                else: pointer1 = pointer1+1

        return ans




