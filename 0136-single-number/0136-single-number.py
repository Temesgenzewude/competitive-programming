class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count=defaultdict(int)
        
        for num in nums:
            count[num]+=1
        
        for key in count:
            if count[key]==1:
                return key