class Solution:
    def select(self, arr, i):
        # code here
        return arr[i]

    def selectionSort(self, arr, n):
        # code here
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for j in range(n):
            print(arr[j], end=" ")
        print()