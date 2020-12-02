class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        #print("%d"%self.val)
#使用插入排序的方法排序链表
class Solution:
    # def sortList(self, head: ListNode) -> ListNode:
    #     #特殊情况
    #     if not head:
    #         return head
    #     #设置一个辅助节点
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     curr = head
    #     while curr.next:
    #         if curr.val<=curr.next.val:
    #             curr = curr.next
    #         else:
    #             #删除该点并存储了该点在变量temp中
    #             temp = curr.next
    #             curr.next = temp.next
    #             #将temp插入合适的位置
    #             pre = dummy
    #             while pre.next:
    #                 if pre.next.val<=temp.val:
    #                     pre = pre.next
    #                 else:
    #                     temp.next = pre.next
    #                     pre.next = temp
    #                     break
    #             curr = head
    #     return dummy.next

    #邮箱发布精选题，设计一个算法，算出 n 阶乘有多少个尾随零。
    def trailingZeroes(self, n: int) -> int:
        #计算n的阶乘
        number=1
        for i in range(1,n+1):
            number=number*i
        #计算尾部有多少个零
        count = 0
        judge = 0
        while not(judge!=0)and number>0:
            yu = number%10
            if yu==0:
                count+=1
            number = number // 10
            judge = yu
        return count

    # 使用归并排序进行链表的排序
    def sortList1(self, head: ListNode) -> ListNode:
        #首先判断该点是不是None或只有一个节点
        if not head or not head.next:
            return head
        #将链表切断
        #'''设置两个点将这个两个点安装二倍的速度进行传递就可以找到中间节点'''
        slow, fast= head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        lift_sort = self.sortList1(head)
        right_sort = self.sortList1(right)
        #merage two link
        re = ListNode(0)
        re1 = re
        while lift_sort and right_sort:
            if lift_sort.val<= right_sort.val:
                re.next = lift_sort
                re = re.next
                lift_sort = lift_sort.next
            else:
                re.next = right_sort
                re = re.next
                right_sort = right_sort.next
        if lift_sort:
            re.next = lift_sort
        if right_sort:
            re.next =right_sort
        return re1.next
    def sortList(self, head: ListNode) -> ListNode:
        #判断没有节点或只有一个节点
        if not head or not head.next:
            return head
        #找到中间节点，并分成两个链表
        fast = head.next
        slow = head
        while fast and fast.next:
            slow =slow.next
            fast = fast.next.next
        mid =slow.next
        slow.next = None
        lift = self.sortList(head)
        right = self.sortList(mid)
        #定义一个辅助节点
        m = ListNode(0)
        h = m
        while lift and right:
            if lift.val<=right.val:
                m.next = lift
                lift = lift.next
            else:
                m.next = right
                right = right.next
            m = m.next
        if lift:
            m.next = lift
        if right:
            m.next =right
        return h.next
    #删除链表中的节点
    '''#该题是只给你这个链表的要删除的节点
        #直接拿来用'''
    def deleteNode(self, node:ListNode):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    head = ListNode(4)
    head1 = ListNode(2)
    head2 = ListNode(1)
    head3 = ListNode(3)
    head.next = head1
    head1.next = head2
    head2.next = head3
    head3.next = None
    te = Solution()
    te = Solution()
    r=te.sortList1(head)
    while r!=None:
        print(r.val)
        r= r.next