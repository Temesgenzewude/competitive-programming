class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def helper(idx, seq):
            if len(seq)>=2:
                result.add(tuple(seq))
            if idx >=len(nums):
                return
            
            for i in range(idx, len(nums)):
                if seq and seq[-1] > nums[i]:
                    continue
                seq.append(nums[i])
                helper(i+1, seq)
                seq.pop()
        
        result=set()
        helper(0,[])
        solution = []
        for res in result:
            solution.append(list(res))
        
        return solution
