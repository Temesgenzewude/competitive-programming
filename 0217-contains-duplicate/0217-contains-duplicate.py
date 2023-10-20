class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1 
            else:
                d[i] = d[i]+1 
        if all(d[i]==1 for i in nums):
            return False
        else:
            return True