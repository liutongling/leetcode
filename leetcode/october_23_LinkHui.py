class ListNode:
    def __init__(self,x: int,nex: ListNode):
        self.val = x
        self.next = nex
class Solution:
    def isPalindrome(self,head:ListNode)->bool:
        #寻找尾节点
        temp = []
        head_temp = head.next
        while head_temp!= None:
            temp.append(head_temp.val)
            head_temp = head_temp.next
        for i in range(len(temp)/2):
            if temp[i] ==temp[-i+len(temp)-1]:
                continue
            else:
                break
        if i == len(temp)/2-1:
            return True
        else:
            return False