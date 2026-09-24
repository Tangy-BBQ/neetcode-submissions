# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we also need a carry bit
        # we can do this in place if we update a list on the way
        # this may need new nodes
        
        # main thing is to not forget our last top node
        
        tp = ListNode(0, l1)
        bp = ListNode(0, l2)
        head = tp
        top = tp
        bottom = bp
        carry = 0
        while top or bottom:
            # print(top.val, bottom.val)
            cur = top.val + bottom.val + carry
            if cur >= 10:
                top.val = cur-10
                carry = 1
            else:
                top.val = cur
                carry = 0
            if top.next and bottom.next:
                top = top.next
                bottom = bottom.next
                continue
            elif top.next:
                top = top.next
                bottom.next = ListNode(0, None)
                bottom = bottom.next
                continue
                
            elif bottom.next:
                top.next = ListNode(0, None)
                top = top.next
                bottom = bottom.next
                continue
            # we have nothing left
            if carry:
                top.next = ListNode(carry, None)
                return head.next
            else:
                return head.next
            
                
            