class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        win_sum=0
        count=0
        n=len(arr)
        
        for i in range(k):
            win_sum+=arr[i]
        if (win_sum // k)>=threshold:
            count+=1
        
        
            
        
        for j in range(n-k):
            win_sum=win_sum - arr[j] + arr[j+k]
            print(win_sum)
            if (win_sum // k)>=threshold:
                count+=1
        
        return count
            
         
        
        
        
        