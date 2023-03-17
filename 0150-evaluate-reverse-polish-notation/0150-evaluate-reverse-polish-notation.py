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
    
#      def calculate(a, b, opt):
#             if opt=="+":
#                 return b+a
#             elif opt=="-":
#                 return b-a
#             elif opt=="*":
#                 return b*a
#             elif opt=="/":
#                 return int(b/a)
            
        
#         stack=[]
        
#         for token in tokens:
            
#             if token in "+-/*":
#                 stack.append(calculate(stack.pop(), stack.pop(), token))
#             else:
#                 stack.append(int(token))
                
                
                
        
        
        