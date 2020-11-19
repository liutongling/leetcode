#合并两个有序链表
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0,None)
        temp = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                temp.next = l1
                temp = l1
                l1 = l1.next
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next
        while l1 != None:
            temp.next = l1
            temp = l1
            l1 = l1.next
        while l2 != None:
            temp.next = l2
            temp = l2
            l2 = l2.next