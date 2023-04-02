class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def quickSort(start, end,arr):
            
            if end-start <= 0:
                return 
            random_pivot_index = random.randint(start, end)
            nums[random_pivot_index], nums[start] = nums[start], nums[random_pivot_index]
            pivot = nums[start]
            write = start + 1

            for read in range(start+1, end+1):
                if nums[read] <= pivot:
                    nums[write], nums[read] = nums[read], nums[write]
                    write += 1
            nums[start], nums[write-1] = nums[write-1], nums[start]
            
            quickSort(start, write-2, arr)
            quickSort(write, end, arr)
            
            
        quickSort(0, len(nums)-1, nums)
            
            
            
           
                
            
        