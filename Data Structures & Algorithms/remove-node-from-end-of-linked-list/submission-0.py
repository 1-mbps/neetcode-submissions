# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> 4
# 2 -> 3 -> 4 -> 1

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return head
        
        ptr = head
        llist = None
        while ptr:
            llist = ListNode(val=ptr.val, next=llist)
            ptr = ptr.next

        ptr = llist
        new_llist = None
        c = 1
        while ptr:
            if c != n:
                new_llist = ListNode(val=ptr.val, next=new_llist)
            ptr = ptr.next
            c += 1

        return new_llist
        