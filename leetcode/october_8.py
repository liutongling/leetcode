class item (object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SLinkList(object):
    '''
    静态链表，就是用数组来模拟链表，那么数组的下标就当做是节点的地址，
    这个概念是静态链表的核心
    '''
    def __init__(self, size = 100):
        '''
        初始化主要是用于初始化链表的大小，而非创建链表
        '''
        self.link = [item(None) for i in range(size + 1)]    # 申请size大小的节点空间[0,1,2,...,size]，其中下标0的节点作为头结点
        self.link[0].next = None    # 表示空表
        self.link[0].space = 1   # 指向第一个节点，因为初始化时第一个节点为空闲节点

        i = 1
        while i < size:
            self.link[i].next = i+1    # 利用空闲节点连成一个新的表，并且头结点的space始终指向下一个空闲的节点
            i += 1

        self.link[i].next = None    # 空闲表尾指向None

        self.length = 0    # 链表长度
        self.rear = 0    # 表尾指针

    def CreateSLinkList_R(self, data):
        '''
        用尾插法创建链表
        '''
        if self.length > 0:     # 非空表无需创建
            print("THIS SLINKLIST IS NOT NULL")
            return

        for each in data:
           if not self.Append(each):
               print("CreateR: NO SPACE!")
               return


    def CreateSLinkList_F(self, data):
        '''
        用头插法创建链表
        '''
        if self.length > 0:     # 非空表无需创建
            print("THIS SLINKLIST IS NOT NULL")
            return

        self.Append(data[0])    # 先添加第一个节点
        for each in data[1:]:    # 在第一个位置前插入
            if self.InsertBefore(each, 1) == 'NS':
                print("CreateF: NO SPACE!")


    def LocateElement(self, data):
        '''
        定位第一个与data值相同的节点，并返回该节点的下标
        '''
        i = self.link[0].next
        while i and self.link[i] != data:
            i = self.link[i].next
        return i

    def Malloc_SL(self):
        '''
        类似于C中malloc函数申请空间，返回空闲节点的下标
        '''
        i = self.link[0].space
        if self.link[0].space:
            self.link[0].space = self.link[i].next

        return i

    def Free_SL(self, k):
        '''
        释放空间，并返回下标k节点的值
        '''
        self.link[k].data = None
        self.link[k].next = self.link[0].space
        self.link[0].space = k

    def DeleteElement(self, data):
        '''
        删除第一个匹配到的节点，并返回删除节点的下标
        '''
        prior = index = 0
        while index != None and self.link[index].data != data:
            prior = index
            index = self.link[index].next

        if not index:
            print("DELETE:\tNot Found!")
            return False

        if not self.link[index].next:    # 判断是否是删除表尾元素，是则改变表尾指针
            self.rear = prior

        self.link[prior].next = self.link[index].next
        self.length -= 1
        self.Free_SL(index)
        return index

    def InsertBefore(self, data, k):
        '''
        在第k个元素前插入元素, 并返回新节点下标
        '''
        if self.link[0].space == None:    # 表满
            print("no space!!!")
            return "NS"

        if k <= 0 or k > self.length:  # 超出当前链表可插入范围
            print("out of range!!!")
            return "OFR"

        count = 0
        index = 0
        while count < k - 1 :    # 找到第k-1个节点，直接在改节点后插入新的元素
            index = self.link[index].next
            count += 1

        node_index = self.Malloc_SL()    # 申请一个新的节点
        self.link[node_index].data = data    # 写入数据
        self.link[node_index].next = self.link[index].next    # 将新节点的next指向第k个节点
        self.link[index].next = node_index    # 将第k-1个节点的next指向新节点node_index
        self.length += 1
        return node_index

    def Append(self, data):
        '''往链表表尾添加元素, 并返回新添加元素的下标'''
        node_index = self.Malloc_SL()

        if not node_index:
            print("Append: NO SPACE!")
            return False

        self.link[node_index].data = data
        self.link[node_index].next = None
        self.link[self.rear].next = node_index
        self.rear = node_index
        self.length += 1
        return node_index

    def Walk(self):
        '''打印链表中所有元素'''
        print("WALK:\t", end = '')
        index = self.link[0].next
        while index:
            print(self.link[index].data, end = '')
            index = self.link[index].next
        print("")

    def Detail(self):
        '''输出链表中各元素的详细信息'''
        print("\nDETAIL:")
        index = self.link[0].next
        count = 1
        while index:
            print("SN:\t%d\tDATA:\t%s\tADDR:\t%d\tNEXT:\t%s" % \
                (count, self.link[index].data, index, str(self.link[index].next)))
            index = self.link[index].next
            count += 1

        print("Length:\t%d\nRear:\t%d\n" % (self.length, self.rear))


if __name__ == '__main__':
    SL = SLinkList()
    while True:
        print()
        opt = input("请选择创建链表的方式： 1. 尾插法 2. 头插法\nOPTION:\t")
        if opt == '1':
            data_str = input("INPUT DATA:\t")
            SL.CreateSLinkList_R(data_str)
            break
        elif opt == '2':
            data_str = input("INPUT DATA:\t")
            SL.CreateSLinkList_F(data_str)
            break
        else:
            print("请做出正确选择！")
            continue

    while True:
        opt = input("\n请选择操作： 1. 插入数据 2. 删除数据 3. 遍历链表 4. 查看链表详细结构 5. 在链表末尾添加数据 6. 退出程序\nOPTION:\t")
        if opt == '1':
            data_str = input("请输入插入数据：\t")
            pos = input("请输入插入位置：\t")
            node_addr = SL.InsertBefore(data_str[0], int(pos))
            if node_addr != 'NS' and node_addr != 'OFR':
                print("成功删除元素%s，元素地址为：%d" % (data_str[0], node_addr))
            else:
                print("INSERT ERROR!!!")

        elif opt == '2':
            data_str = input("请输入删除数据：\t")
            data_pos = SL.DeleteElement(data_str[0])
            if data_pos:
                print("成功删除元素%s，元素地址为：%d" % (data_str[0],data_pos))

        elif opt == '3':
            print('')
            SL.Walk()
        elif opt == '4':
            SL.Detail()
        elif opt == '5':
            data_str = input("请输入数据:\t")
            node_addr = SL.Append(data_str[0])
            print("成功添加元素：\t%s\t元素地址为：\t%d" % (data_str[0], node_addr))
        elif opt == '6':
            break
        else:
            print("请做出正确选择！")