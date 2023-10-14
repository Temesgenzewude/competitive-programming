class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1],[1,1]]
        if rowIndex==0:
            return triangle[0]
        if rowIndex==1:
            return triangle[1]
        curr = []
        prev = [1,1]
        i = 2
        while i<=rowIndex:
            for j in range(i+1):
                if j==0 or j==i:
                    curr.append(1)
                else:
                    curr.append(prev[j-1]+prev[j])
            prev = curr
            curr = []
            i+=1
        return prev
        