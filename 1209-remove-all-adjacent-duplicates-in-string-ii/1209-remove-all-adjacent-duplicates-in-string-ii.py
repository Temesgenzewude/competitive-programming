class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["!", 1]]
        for elem in s:
            if elem == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([elem, 1])
            
            while stack[-1][1] >= k:
                stack[-1][1] -= k
                if stack[-1][1] == 0: stack.pop()
             
        return "".join(i*j for i, j in stack[1:])
        