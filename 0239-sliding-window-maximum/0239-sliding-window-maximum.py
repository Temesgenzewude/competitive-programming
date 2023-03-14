class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue=deque()
        result=[]
        n=len(nums)
        
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
        result.append(nums[queue[0]])
        
        
            
        
        
        
        for j in range(k,n):
            while queue and (j-k+1 >queue[0]):
                queue.popleft()
                
        
            
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            
            queue.append(j)
            result.append(nums[queue[0]])
        
        return result
                
                
            
        
        
        
        
        
#         count = Counter(nums[:k])
#         max_ = max(nums[:k])
#         ans = [max_]
#         left = 0
#         for right in range(k, len(nums)):
#             count[nums[right]] += 1
#             count[nums[left]] -= 1
#             if not count[nums[left]]:
#                 del count[nums[left]]
            
#             if nums[left] == max_:
#                 max_ = max(count)
#             if nums[right] > max_:
#                 max_ = nums[right]
                
#             ans.append(max_)
#             left += 1
            
        return ans
        
            
        
        
        
        
        
        
        
        
        
#         max_ = max(nums[:k])
#         ans = [max_]
# #         wrong - does not work for every test case
#         for i in range(k, len(nums)):
#             max_ = max(max_, nums[i])
#             ans.append(max_)
#         return ans
        
        
        
        
        
        
        # for i in range(len(nums) - k + 1):
        #     ans.append(max(nums[i:i + k]))
        # return ans
    
#         for i in range(len(nums) - k + 1):
#             max_ = float('-inf')
            
#             for j in range(i, i + k):
#                 max_ = max(max_, nums[j])
                
#             ans.append(max_)
            
#         return ans