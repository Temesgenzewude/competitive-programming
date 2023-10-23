class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        dc=defaultdict(lambda:0)
        for a in nums1:
            dc[a]=1
        nums2=set(nums2)
        for a in nums2:
            if(dc[a]==1):
                ans.append(a)
        return ans