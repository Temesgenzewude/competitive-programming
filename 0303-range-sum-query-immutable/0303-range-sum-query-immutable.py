class NumArray:

    def __init__(self, nums: List[int]):
        
        self.nums=nums
        self.cum=[0] + list(accumulate(nums))
        
        

    def sumRange(self, left: int, right: int) -> int:
        return self.cum[right+1] - self.cum[left]
#         prefixSum=[self.nums[0]]
        
#         for i in range(1, len(self.nums)):
#             prefixSum.append(prefixSum[i-1] + self.nums[i])
#         if left == 0:
#             return prefixSum[right]
#         else:
#             return prefixSum[right] - prefixSum[left-1] 
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)