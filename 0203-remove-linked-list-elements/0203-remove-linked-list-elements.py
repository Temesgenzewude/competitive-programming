# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy=ListNode(0, head)
        prev, curr=dummy, head
        
        while curr:
            temp=curr.next
            
            if curr.val==val:
                prev.next=temp
            else:
                prev=curr
            curr=curr.next
        
        return dummy.next
    
            
         
            
          
                
        
        