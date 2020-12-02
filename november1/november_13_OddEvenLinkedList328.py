class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        elif not head.next:
            return head
        postion = 1
        head1 = ListNode()
        head2 = ListNode()
        ye = head1
        ye1 = head2
        while head!=None:
            if postion%2==1:
                head1.val = head.val
                x = head1
                temp = ListNode()
                head1.next = temp

                head1=temp
                head = head.next
                postion+=1
            else:
                head2.val = head.val
                y = head2
                temp = ListNode()
                head2.next = temp
                head2 = temp
                head = head.next
                postion+=1
        y.next =None
        x.next = ye1
        return ye

    def generate(self, numRows: int) -> list:
        numRows += 1
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        else:
            listGerate = [[1], [1, 1]]
            for i in range(2, numRows -1):
                k = [i for i in range(i+1)]
                for j in range(i+1):
                    if j == 0 or j == i:
                        k[j] = 1
                    else:
                        k[j] = listGerate[i - 1][j - 1] + listGerate[i - 1][j]
                listGerate.append(k)
        return listGerate

if __name__ == '__main__':
    # head = ListNode()
    # head.val = 1
    # head1 =  ListNode()
    # head1.val = 2
    # head.next = head1
    # head2 = ListNode()
    # head2.val = 3
    # head1.next = head2
    # head3 = ListNode()
    # head3.val = 4
    # head2.next = head3
    # head3.next=None
    # test = Solution()
    # ye = test.oddEvenList(head)
    # while ye:
    #     print(ye.val)
    #     ye = ye.next
    s = Solution()
    print(s.generate(6))