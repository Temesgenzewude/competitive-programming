
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n=len(nums)
        lst=[0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if nums[j]<nums[i]:
                    lst[i]+=1
        return lst
def main():
    nums = [8,1,4,2,3]
    result=Solution().smallerNumbersThanCurrent(nums)
    print(result)
main()