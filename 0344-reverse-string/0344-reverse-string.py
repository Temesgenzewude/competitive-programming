class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        
        while right>=left:
            s[right], s[left]=s[left], s[right]
            left+=1
            right-=1
            
        