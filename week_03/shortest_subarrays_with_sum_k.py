from collections import deque


class Solution:
    def shortestSubarray(self, nums, k: int) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + nums[i - 1]
        result = len(nums) + 1
        q = deque()
        for i in range(len(dp)):
            while q and dp[i] - dp[q[0]] >= k:
                result = min(result, i - q.popleft())
            while q and dp[i] < dp[q[-1]]:
                q.pop()
            q.append(i)

        return result if result != len(nums) + 1 else -1


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2]
    k = 4
    print(sol.shortestSubarray(nums, k))
    nums = [2, -1, 2]
    k = 3
    print(sol.shortestSubarray(nums, k))
    nums = [1]
    k = 1
    print(sol.shortestSubarray(nums, k))
