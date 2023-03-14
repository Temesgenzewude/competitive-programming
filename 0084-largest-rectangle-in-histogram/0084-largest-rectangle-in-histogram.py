class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-float("inf"))
        mono_stack=[]
        longest_rect=0
        
        for idx, height in enumerate(heights):
            left_bound=idx
            
            
            
            
            
            
            while mono_stack and heights[mono_stack[-1][0]]> height:
                
        
                curr_cand=mono_stack.pop()
               
                left_bound=curr_cand[1]
                longest_rect=max(longest_rect, (idx-left_bound)*heights[curr_cand[0]])
            mono_stack.append((idx,left_bound))
        
        return longest_rect
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
        
        
        
        
        
        
        
        
        
        
        
            
            
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        