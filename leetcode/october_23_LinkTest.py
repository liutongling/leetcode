#本次任务实现链表的创建和打印
class ListNode:
    def __init__(self,val:int):
        self.next = None
        self.val = val
class ListFunction:
    #创建一个链表
    def create(self,long:int)->ListNode:
        head = ListNode(0)
        temp = head
        #创建一个存储列表的元组
        for i in range(long):
            x = int(input("请输入第%d个元素的值" %(i+1)))
            point = ListNode(x)
            temp.next = point
            temp = point
        return head
    #插入一个数值
    def insert(self,k:int,head:ListNode):
        pass
    #将链表进行遍历输出
    def query(self,head:ListNode):
        temp = head.next
        while temp != None:
            print("值为%d" %(temp.val))
            temp = temp.next
if __name__ == '__main__':
    test = ListFunction()
    head = test.create(5)
    test.query(head)