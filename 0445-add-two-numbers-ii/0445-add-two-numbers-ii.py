# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev1=None
        curr1=l1
        len1=0
        
        while curr1:
            temp1=curr1.next
            curr1.next=prev1
            prev1=curr1
            curr1=temp1
            len1+=1
            
        prev2, curr2, len2=None, l2,0
        while curr2:
            temp2=curr2.next
            curr2.next=prev2
            prev2=curr2
            curr2=temp2
            len2+=1
                  
        n=min(len1, len2)
    
        cary=0  
        l1, l2 = prev1, prev2
        for i in range(n):
            sum_=prev1.val+prev2.val+cary
            cary=sum_//10
            if len1 > len2:
                prev1.val= sum_%10
            else:
                prev2.val=sum_%10
        
            
            prev1=prev1.next
            prev2=prev2.next
        if cary >0:
            if prev1:
                while prev1:
                    sum_=prev1.val+cary
                    cary=sum_//10
                    prev1.val=sum_%10
                    prev1=prev1.next
            if prev2:
                while prev2:
                    sum_=prev2.val+cary
                    cary=sum_//10
                    prev2.val=sum_%10
                    prev2=prev2.next
        
       
            
        
        prev, curr=None, l1 if len1 > len2 else l2
        
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        if cary > 0:
            head=ListNode(cary)
            head.next=prev
            return head
        return prev
                    
                
        
    
                
                
            
       
        
        
            
        
        
        
        