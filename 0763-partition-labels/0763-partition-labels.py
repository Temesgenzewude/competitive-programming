class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndecies={}
        for idx, char in enumerate(s):
            lastIndecies[char]=idx
        
        result=[]
        size, end=0, 0
        
        for idx, char in enumerate(s):
            size +=1
            end=max(end, lastIndecies[char])
            
            if idx == end:
                result.append(size)
                size=0
        return result
        