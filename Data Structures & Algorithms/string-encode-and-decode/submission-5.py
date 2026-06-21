class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for items in strs:
            result+=items +'~'
        return result
        
    def decode(self, s: str) -> List[str]:
        
        ans=[]
        b=''
        for word in s:
            if word=='~':
                ans.append(b)
                b=''
            else:
                b+=word
        
        return ans
        


            
            


