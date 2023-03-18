class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        
        stack=[]
        curr_path=""
        
        for pth in path+'/':
        
            if pth=='/':
                if curr_path=="..":
                    if stack: stack.pop()
                elif curr_path!="" and curr_path !=".":
                    stack.append(curr_path)
                curr_path=""
            else:
                curr_path+=pth
        
        return '/'+'/'.join(stack)
        