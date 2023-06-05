class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        result=[]
        length =len(arr)
        for i in range(length, 0, -1):
            pos = arr.index(i)
            if pos == i - 1:
                continue
            if pos != 0:
                result.append(pos + 1)
                arr[:pos + 1] = arr[:pos + 1][::-1]
            result.append(i)
            arr[:i] = arr[:i][::-1]
        return result
        
        
#         n=len(arr)
#         flips=[]
        
#         for i in range(n):
#             curr_max=max(arr[:n-i])
#             curr_max_idx=arr.index(curr_max)
#             arr[:curr_max_idx]=reversed(arr[:curr_max_idx])
            
#             flips.append(curr_max_idx)
            
#             arr[:n-i]=reversed(arr[:n-i])
#             flips.append(n-i)
            
#         return flips