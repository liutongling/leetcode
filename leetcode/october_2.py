#定义一个链表
class ListNode():
    def __init__(self,number:int,listnode:ListNode):
        self.number = number
        self.listnode = listnode
class Solution():
    def addTwoNumbers(self,l1:ListNode,l2:ListNode) ->ListNode:
        l3 = ListNode()
        l3.number = 0
        l3.listnode=None
        count = 0
        while l1 != None and l2 !=None:
            if l1.number+l2.number > 10:
                l3.number = (l1.number+l2.number)%10 + count
                count = 1
            elif l1.number+l2.number < 10:
                l3.number = l1.number+l2.number
                count = 0
            l1 = l1.listnode
            l2 = l2.listnode


        return