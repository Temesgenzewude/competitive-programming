'''
An integer array original is transformed into
a doubled array changed by appending twice the value of
every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is
a doubled array. If changed is not a doubled array,
 return an empty array. The elements in original may be returned in any order.

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

Constraints:
1 <= changed.length <= 105
0 <= changed[i] <= 105
'''

from collections import deque
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        # if len(changed) == 1 or len(changed) == 0 or len(changed) % 2 != 0:
        #     return []
        # doubled = []
        # for num in changed:
        #     if num % 2 == 0:
        #         doubled.append(num)
        # if len(doubled) < (len(changed) / 2):
        #     return []
        # result = []
        # for num in changed:
        #     for double in doubled:
        #         if num == double:
        #             continue
        #         if num * 2 == double:
        #             if len(result) == len(changed) / 2:
        #                 return result
        #             result.append(double // 2)
        # return result if len(result) == len(changed) / 2 else []

        if len(changed) == 1 or len(changed) == 0 or len(changed) % 2 != 0:
            return []

        # dic = {}
        # for i in range(len(changed)):
        #     if changed[i] in dic:
        #         dic[changed[i]] += 1
        #     else:
        #         dic[changed[i]] = 1
        #
        # changed.sort()
        # print(changed)
        # print(dic)
        #
        # result = []
        # for i in range(len(changed)):
        #     freq = dic[changed[i]]
        #     if freq > 0:
        #         result.append(changed[i])
        #         dic[changed[i]] -= 1
        #     double = 2 * changed[i]
        #     print(double, changed[i])
        #     dic[double] -= 1
        #
        # return result

        answer = []
        que = deque()

        for num in sorted(changed):
            if que and num == que[0]:
                que.popleft()
            else:
                que.append(num * 2)
                answer.append(num)

        return [] if que else answer


def main():
    sol = Solution()
    test3 = [0, 0, 0, 0]
    test4 = [0, 0, 2, 1]
    arr = [4, 1, 2, 2, 2, 4, 8, 4]

    test2 = [6, 3, 0, 1]
    test = [1, 3, 4, 6, 8, 2]
    nums = [1, 2, 7, 4, 0, 2, 6, 5, 9]
    nums2 = [6, 2, 3, 1, 10, 5, 7]
    num3 = [1]
    print(sol.findOriginalArray(test3))


main()
