#User function Template for python3

class Solution: 
    def select(self, arr, i):
        index=i
        for j in range(i,n):
            if arr[j] < arr[index]:
                index=j
                
        return index

    
    def selectionSort(self, arr,n):
        for i in range(n):
            index=self.select(arr,i)
            arr[i], arr[index]= arr[index],arr[i]
            
                
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends