class Solution(object):
    def targetIndices(self, nums, target):
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(n - 1):
                if nums[j + 1] < nums[j]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]

        for k in range(n):
            if nums[k] == target:
                result.append(k)
        return result


def main():
    nums = [1, 2, 5, 2, 3]
    target = 2
    result = Solution().targetIndices(nums, target)
    print(result)


main()