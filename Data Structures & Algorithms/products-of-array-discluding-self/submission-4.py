class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product =1
        for i in nums:
            if i!=0:
                product*=i

        number_of_zeros = nums.count(0)

        if number_of_zeros == 0:
            for i in nums:
                a = product/i
                result.append(int(a))
        elif number_of_zeros == 1:
            for i in nums:
                if i==0:
                    result.append(int(product))
                else: result.append(0)
        else:
            for i in nums:
                result.append(0)
        return result

            
                