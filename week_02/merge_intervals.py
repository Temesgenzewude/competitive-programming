'''
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals,
and return an array of the non-overlapping
intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # res=[]
        # for i in range(len(intervals)-1):
        #     if intervals[i][1]>=intervals[i+1][0]:
        #         lst=[intervals[i][0], intervals[i+1][1]]
        #         res.append(lst)
        #     else:
        #         res.append(intervals[i])
        # return res

        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for interval in intervals:
            newInterval = interval
            if res:
                if res[-1][1] >= interval[0]:
                    newInterval = res.pop()
                    if interval[1] > newInterval[1]:
                        newInterval[1] = interval[1]
            res.append(newInterval)
        return res


def main():
    sol = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(sol.merge(intervals))


main()
