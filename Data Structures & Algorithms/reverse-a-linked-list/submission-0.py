# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3

def build_linked_list(vals: list, index: int):
    if index < 0:
        return None
    return ListNode(val=vals[index], next=build_linked_list(vals, index-1))

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        lst = []

        nxt = head

        while nxt:
            lst.append(nxt.val)
            nxt = nxt.next

        llist = ListNode(val=lst[-1], next=build_linked_list(lst, len(lst)-2))

        return llist
        
            

        