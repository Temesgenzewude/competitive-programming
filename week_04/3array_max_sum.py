
"""
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.



Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3
"""


class Solution:
  def maxSumOfThreeSubarrays(self, nums, k: int):
    ans = [-1] * 3
    subarrayCount = len(nums) - k + 1
    dp = [0] * subarrayCount
    sum = 0

    for i, num in enumerate(nums):
      sum += num
      if i >= k:
        sum -= nums[i - k]
      if i >= k - 1:
        dp[i - k + 1] = sum

    left = [0] * subarrayCount
    maxIndex = 0

    for i in range(subarrayCount):
      if dp[i] > dp[maxIndex]:
        maxIndex = i
      left[i] = maxIndex

    right = [0] * subarrayCount
    maxIndex = subarrayCount - 1

    for i in reversed(range(subarrayCount)):
      if dp[i] >= dp[maxIndex]:
        maxIndex = i
      right[i] = maxIndex

    for i in range(k, subarrayCount - k):
      if ans[0] == -1 or dp[left[i - k]] + dp[i] + dp[right[i + k]] > dp[ans[0]] + dp[ans[1]] + dp[ans[2]]:
        ans = [left[i - k], i, right[i + k]]

    return ans