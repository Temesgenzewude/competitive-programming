
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
