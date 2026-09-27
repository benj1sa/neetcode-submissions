# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        l1 = list1
        l2 = list2
        head = merged = ListNode(-1, None) # dummy head

        while l1 and l2:
            insert_node = None
            if l1.val < l2.val:
                insert_node = l1
                l1 = l1.next
            else:
                insert_node = l2
                l2 = l2.next
            merged.next = insert_node
            merged = merged.next
        
        while l1:
            merged.next = l1
            l1 = l1.next
            merged = merged.next
        while l2:
            merged.next = l2
            l2 = l2.next
            merged = merged.next

        return head.next


