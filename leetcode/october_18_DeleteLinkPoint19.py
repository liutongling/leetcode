#删除链表中的倒数第N个节点
#给定一个链表，删除链表的倒数第n个节点，并返回链表的头节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def count(self,head: ListNode)->int:
        nums = 0
        temp = head
        while temp.next!=None:
            nums+=1
            temp=temp.next
        return nums+1
    def tail(self,head:ListNode)->ListNode:
        temp = head
        if temp.next==None:
            return head
        while temp.next!=None:
            temp=temp.next
        return temp
class Solution(ListNode):
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #存储临时头节点
        temp = head
        pre = 0
        long = self.count(head)
        if n<=0 or n>long:
            return head
        if n==1:
            pre = long-1
            i = 1
            while i<=pre:
                temp=temp.next
            temp.next=None
            return head
        if n==long:
            temp =temp.next
            return temp
        pre = -n+long+1
        k = 1
        while k<pre:
            temp=temp.next
        temp.next = temp.next.next
        return head

#正确答案(leecode)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next