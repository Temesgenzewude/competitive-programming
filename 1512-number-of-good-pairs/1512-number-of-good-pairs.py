class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count= defaultdict(int)
        
        for num in nums:
            count[num]+=1
        
        
        goodPairs=0
        for key in count:
            n= count[key]
            res=(n*(n-1))//2
            goodPairs+=res
        
        
        return goodPairs
            
        
        
        