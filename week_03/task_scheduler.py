
'''
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1], k = 1
Output: 1
Example 2:
Input: nums = [1,2], k = 4
Output: -1
Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3

Constraints:
1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
'''
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        count = Counter(tasks)
        maxFre = max(count.values())
        maxFreqTaskOccupy = (maxFre - 1) * (n + 1)
        nMaxFreq = sum(value == maxFre for value in count.values())
        return max(maxFreqTaskOccupy + nMaxFreq, len(tasks))


if __name__ == '__main__':
    sol = Solution()
    tasks1 = ["A", "A", "A", "B", "B", "B"]
    n1 = 2
    print(sol.leastInterval(tasks1, n1))
    tasks2 = ["A", "A", "A", "B", "B", "B"]
    n2 = 0
    print(sol.leastInterval(tasks2, n2))
    tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n = 2
    print(sol.leastInterval(tasks, n))
