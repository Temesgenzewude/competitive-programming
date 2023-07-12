class Solution:
    def numDecodings(self, s: str) -> int:
        memo={len(s):1}
        def dfs(index):
            if index in memo:
                return memo[index]
            if s[index]=="0":
                return 0
            result=dfs(index+1)
            if (index+1 < len(s) and (s[index]=="1" or s[index]=="2" and s[index+1] in "0123456")):
                result+=dfs(index+2)
            memo[index]=result
            return memo[index]
        
        return dfs(0)