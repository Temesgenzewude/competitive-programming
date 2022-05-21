class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k > len(nums):
            return "INVALID INPUT FOR K"
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                if num not in dic:
                    dic[num] = 0
                dic[num] = 1
        dic = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        return [item[0] for item in dic][: k]


def main():
    sol = Solution()
    nums = [1, 2, 3, 1, 1, 3]
    nums2 = [1, 1, 1, 1]
    num1 = [1]
    arr = [3, 2, 4, 1, 1, 4, 5]
    arr2 = [1, 2, 3, 3, 5, 6, 3, 2]
    print(sol.topKFrequent(num1, 1))
    # print(sol.topKFrequent(arr, 3))


main()
