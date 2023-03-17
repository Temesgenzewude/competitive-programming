class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        
        stack=[]
        
        for i in range(len(tokens)):
            if tokens[i]=="/":
                opera1=stack.pop()
                opera2=stack.pop()
                stack.append(int(opera2/opera1))
            
                
            elif tokens[i]=="*":
                opera1=stack.pop()
                opera2=stack.pop()
                stack.append(opera1*opera2)
            
                
            elif tokens[i]=="+":
                opera1=stack.pop()
                opera2=stack.pop()
                stack.append(opera1+opera2)
                
            elif tokens[i]=="-":
                opera1=stack.pop()
                opera2=stack.pop()
                stack.append(opera2-opera1)
            
            else:
                stack.append(int(tokens[i]))
        
        
        return stack.pop()
                
                
                
        
        
        