class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax=-1
        n=len(arr)
        
        for i in range(n-1,-1,-1):
            newMax=max(rightMax, arr[i])
            arr[i]=rightMax
            rightMax=newMax
        return arr
        