class Solution(object):
    def kClosest(self, points, k):
        points.sort(key=lambda k : k[0]**2 + k[1]**2)
        return points[:k]


def main():
    sol=Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    k=2
    result=sol.kClosest(points, k)
    print(result)
main()
