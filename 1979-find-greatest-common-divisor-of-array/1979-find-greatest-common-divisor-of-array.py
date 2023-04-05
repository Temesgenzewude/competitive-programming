class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        larg, small= max(nums), min(nums)
        while small != 0:
            temp = small
            small = larg % small
            larg = temp

        return larg
            
        
        
        