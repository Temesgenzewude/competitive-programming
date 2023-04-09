class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        peak=arr[1]
        nex=0
        if (arr[0] >= arr[1]):
            print(peak)
            return False
        
        
        for i in range(2,len(arr)):
            if arr[i] > peak:
                peak=arr[i]
            elif arr[i]==peak:
                print(peak)
                return False
            elif arr[i] < peak:
                nex=i
                break
       
        for j in range(nex, len(arr)):
            if arr[j] >=peak:
                return False
            peak=arr[j]
        
        return True
    
        
                
            
        
        
        