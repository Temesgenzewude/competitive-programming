class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]<nums[j]:
                    nums[i], nums[j]=nums[j], nums[i]
                elif nums[i]>nums[j]:
                    continue

def main():
    nums=[1,2, 0, 0, 1, 2, 1]
    solution=Solution()
    solution.sortColors(nums)
main()
