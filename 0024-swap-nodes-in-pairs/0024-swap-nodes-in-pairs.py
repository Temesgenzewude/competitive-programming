# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nxt
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        else :
            head.val,head.next.val=head.next.val,head.val
            self.swapPairs(head.next.next)
        return head
        
        
            
        
        
        
        
        # cu = head
        # while head.next:
        #     l = ListNode(head.val,None)
        #     l1 =  ListNode(head.next.val,None)
        #     l2 = head.next.next
        #     l.next = l2
        #     l1.next = l
        #     head = l1
        #     head = head.next.next
        # return cu
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        