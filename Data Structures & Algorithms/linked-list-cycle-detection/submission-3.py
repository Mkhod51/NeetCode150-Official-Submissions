# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False 
            
        slow = head 
        fast = head.next

        while True:
            if fast == None or fast.next == None:
                return False 

            if fast.val == slow.val:
                return True 

            fast = fast.next.next 
            slow = slow.next 
            
                
