class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        def mergeSort(arr, left, right):
            if left==right:
                return [arr[left]]
            mid=left + (right-left)//2
            
            left_half=mergeSort(arr, left, mid)
            right_half=mergeSort(arr, mid+1, right)
            
            return merge(left_half, right_half)
        
        def merge(left_half, right_half):
            left_ptr=right_ptr=0
            res=[]
            
            while left_ptr < len(left_half) and right_ptr < len(right_half):
                if left_half[left_ptr] <= right_half[right_ptr]:
                    res.append(left_half[left_ptr])
                    left_ptr+=1
                else:
                    res.append(right_half[right_ptr])
                    right_ptr+=1
            
            res.extend(left_half[left_ptr:])
            res.extend(right_half[right_ptr:])
            
            return res
        
        sorted_arr= mergeSort(nums, 0, len(nums)-1)
        
        print(sorted_arr)
        
        result=[]
        
        for i in range(len(nums)):
            if sorted_arr[i]==target:
                
                result.append(i)
        
        return result
                
        