class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        self.pairs=0
        def mergeSort(left,right, arr):
            if left==right:
                return [arr[left]]
            
            mid=left + (right-left)//2
            
            left_half=mergeSort(left, mid,arr)
            right_half=mergeSort(mid+1, right, arr)
            
            return merge(left_half, right_half)
        def merge(left_half, right_half):
            result=[]
            
            right=0
            currPairs=0
            for left in range(len(left_half)):
                while right< len(right_half) and left_half[left] > 2* right_half[right]:
                    currPairs+=1
                    right+=1
                self.pairs+=currPairs
                
            left_ptr=right_ptr=0
            while left_ptr < len(left_half) and right_ptr < len(right_half):
                if left_half[left_ptr] <= right_half[right_ptr]:
                    result.append(left_half[left_ptr])
                    left_ptr+=1
                else:
                    result.append(right_half[right_ptr])
                    right_ptr+=1
                    
            result.extend(left_half[left_ptr:])
            result.extend(right_half[right_ptr:])
            
            return result
        
        mergeSort(0, len(nums)-1, nums)
        
        return self.pairs
        