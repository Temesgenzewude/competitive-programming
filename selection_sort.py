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
