class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j  in range(len(nums)):
                if nums[i] +nums[j]==target and i!=j:
                    return i,j
def main():
    lst=[3,2,4]
    target=6
    solution=Solution()
    print(solution.twoSum(lst, target))
main()