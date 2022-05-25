'''
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have
to wait after the ith day to get a warmer temperature. If there is no future
day for which this is possible, keep answer[i] == 0 instead.
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

'''


class Solution:
    def dailyTemperatures(self, temperatures):
        # stack = []
        # answer = []
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             answer.append(j - i)
        #             break
        #         elif j == len(temperatures) - 1:
        #             answer.append(0)
        # answer.append(0)
        # return answer
        stack = []

        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                st=stack.pop()
                temp, index = st[0], st[1]
                result[index] = (i - index)

            stack.append([t, i])

        return result


if __name__ == '__main__':
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temperatures))
    temperatures = [30, 40, 50, 60]
    print(sol.dailyTemperatures(temperatures))
    temperatures = [30, 60, 90]
    print(sol.dailyTemperatures(temperatures))
