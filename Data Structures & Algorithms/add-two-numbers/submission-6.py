# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addIndiv(l1, l2, res, carry):
            if not (l1 or l2): 
                if carry > 0:
                    res.next = ListNode(carry, None)
                return res 
            
            if not l1:
                l1val = 0
                l1next = None
                l2val = l2.val 
                l2next = l2.next 
            elif not l2:
                l2val = 0
                l2next = None 
                l1val = l1.val 
                l1next = l1.next
            else:
                l1val = l1.val 
                l2val = l2.val 
                l1next = l1.next 
                l2next = l2.next 

            sum = l1val + l2val + carry
            res.next = ListNode(sum % 10, None)
            res = res.next 
            return addIndiv(l1next, l2next, res, sum // 10)
        dummy = ListNode()
        tail = addIndiv(l1, l2, dummy, 0)

        return dummy.next
            