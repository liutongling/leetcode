class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def insertionSortList(self, head: ListNode) -> ListNode:
    #     #定一个前驱节点
    #     pre = ListNode(0)
    #     pre.next = head
    #     #第二层循环使用的前驱节点
    #     pretemp = pre
    #     #第一层循环的节点
    #     headnew1 = head
    #     #第一层循环的前驱
    #     pre0 = pre
    #     #定义一个值
    #     minvalue = headnew1.val
    #     #存储这个最小值点
    #     minnote = headnew1
    #     #记录当前最小节点和最小节点的前驱
    #     newpre = pretemp
    #     #使用一个新的节点指向最小的节点
    #     newpre1 = ListNode(0)
    #     h = newpre.next
    #     mi = head
    #     te = head
    #     while headnew1!=None:
    #         minvalue = headnew1.val
    #         te = headnew1
    #         while te!=None:
    #             if te.val < minvalue:
    #                 #minvalue = te.val
    #                 mi = te
    #                 newpre = pretemp
    #                 print(minvalue)
    #             te = te.next
    #             #print(te.val)
    #             print("ni")
    #             pretemp = pretemp.next
    #         print("ni%d"%minvalue)
    #         #使用新的节点指向最小节点
    #         newpre1.next = mi
    #         newpre1 = newpre1.next
    #         #去掉原来链表的最小值
    #         newpre.next = mi.next
    #         #改变headnew1 和它的前驱
    #         headnew1 = headnew1.next
    #         pretemp = pre.next
    #         pre = pre.next
    #     return h

    def insertionSortList(self, head: ListNode) -> ListNode:
        #设置一个初始节点
        demmy = ListNode(0)
        demmy.next = head
        curr = head
        pre = demmy
        while curr.next:
            if curr.val<=curr.next.val:
                curr = curr.next
                #continue
            else:
                #删除当前点
                temp = curr.next
                curr.next = curr.next.next
                pre = demmy
                while pre.next:
                    if pre.next.val<=temp.val:
                        pre =pre.next
                    else:
                        temp.next=pre.next
                        pre.next = temp
                        break
                curr = head#这是因为每次上一个节点有可能会大于后面多个节点的值
        return demmy.next

if __name__ == '__main__':
    #创建一个链表
    head =ListNode(4)
    head1 = ListNode(2)
    head2 = ListNode(1)
    head3 = ListNode(3)
    head.next = head1
    head1.next = head2
    head2.next = head3
    head3.next=None
    te = Solution()
    r = te.insertionSortList(head)
    while r!=None:
        print(r.val)
        r= r.next