class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        seen=defaultdict(int)
        operations=0
        for num in nums:
            if seen[k-num] > 0:
                operations+=1
                seen[k-num]-=1
            else:
                seen[num]+=1
        return operations
        