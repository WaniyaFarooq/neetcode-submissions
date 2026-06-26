class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        p0 = 0
        p1 = len(numbers)-1

        while(p1>p0):
            if numbers[p0]+numbers[p1] == target and p1!=p0: return [p0+1,p1+1]

            elif numbers[p0]+numbers[p1] < target:
                p0=p0+1

            else :p1=p1-1
            print(f"p0 = {p0} p1 = {p1}")

        return []




