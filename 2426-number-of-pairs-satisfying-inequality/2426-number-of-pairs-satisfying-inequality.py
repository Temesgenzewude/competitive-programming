class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        self.count=0
        
        nums=[]
        
        for i in range(len(nums1)):
            nums.append(nums1[i]-nums2[i])
            
        count=0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if i < j and (nums1[i]-nums1[j] <=nums2[i]-nums2[j] + diff):
        #             count+=1
        # return count
        
        def mergeSort(left, right, arr):
            if left==right:
                return [arr[left]]
            mid= left + (right-left)//2
            
            left_half=mergeSort(left,mid,arr)
            right_half=mergeSort(mid+1, right, arr)
            
            return merge(left_half, right_half)
        
        def merge(left_half, right_half):
            result=[]
            
            left=0
            
            newPairs=0
            for right in range(len(right_half)):
                
                while left < len(left_half) and left_half[left]-right_half[right] <=diff:
                    newPairs+=1
                    
                    left+=1
                self.count+=newPairs
                
            
            left_ptr=right_ptr=0
            while left_ptr < len(left_half) and right_ptr < len(right_half):
                if left_half[left_ptr] <=right_half[right_ptr]:
                    result.append(left_half[left_ptr])
                    left_ptr+=1
                else:
                    result.append(right_half[right_ptr])
                    right_ptr+=1
            result.extend(left_half[left_ptr:])
            result.extend(right_half[right_ptr:])
            
            return result
        
        mergeSort(0, len(nums)-1, nums)
        
        return self.count
                    
                    
                
                
                
                
            
            
                
                
                
                
                
        
   
        