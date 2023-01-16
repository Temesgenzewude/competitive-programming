class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange=[0]*1001
        
        for trip in trips:
            numPass, start, end=trip
            
            passChange[start]+=numPass
            passChange[end]-=numPass
            
        currPass=0
        
        for i in range(1001):
            currPass+=passChange[i]
            
            if currPass > capacity:
                return False
        return True
        