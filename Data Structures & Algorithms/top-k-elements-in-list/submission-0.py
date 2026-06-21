class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = set(nums)
        d = {}
        for i in unique_nums:
            d[i]=nums.count(i)
        result = []
        max_num =0
        max_index =0
        while k:
            for key,value in d.items():
                if value>max_num:
                    max_num = value
                    max_index = key
            result.append(max_index)
            d.pop(max_index,None)
            max_num=0
            k=k-1
        return result



        