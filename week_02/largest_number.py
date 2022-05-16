

'''
Given a list of non-negative integers nums,
arrange them such that they form the largest number and return it.

Since the result may be very large,
so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 109
'''

class Solution(object):
    def largestNumber(self, nums):
        current_max, answer = "", ""

        nums = [str(num) for num in nums]
        while nums:
            for num in nums:
                if not current_max:
                    current_max = num
                else:
                    if num + current_max > current_max + num:
                        current_max = num
            answer += current_max
            nums.remove(current_max)
            current_max = ""
        return answer if not answer.startswith("0") else "0"


def main():
    sol = Solution()
    nums = [3, 30, 34, 5, 9]
    print(sol.largestNumber(nums))


main()
