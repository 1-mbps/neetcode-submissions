# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0 -> 1 -> 2 -> 3


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        llist = None
        ptr = head
        while ptr:
            llist = ListNode(val=ptr.val, next=llist)
            ptr = ptr.next

        return llist
            

        
            

        