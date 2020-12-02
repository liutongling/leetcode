#Given a non-negative integer num represented as a string,
# remove k digits from the number so that the new number is the smallest possible.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #此算法可以寻找连续的数值最小
    def removeKdigits(self, num: str, k: int) -> str:
        numNumberList = [int(x) for x in num]
        if k == len(numNumberList):
            return "0"
        minNumber = pow(10,len(numNumberList))
        index = 0
        #从第零删除判断，最高位多少，依次判断，决策出最小数字的最高位
        a_index = [i for i in range(len(numNumberList))]
        a_index = set(a_index)
        for i in range(len(numNumberList)-k+1):
            indexList = []
            for j in range(i,i+k):
                indexList.append(j)
            b_index = set(indexList)
            new_index = a_index-b_index
            a = [numNumberList[i] for i in new_index]
            a = [str(i) for i in a]
            b = int(''.join(a))
            if b < minNumber:
                minNumber = b
        return str(minNumber)
    #贪心算法和最小栈
    def remove(self,num:str,k:int)->str:
        #定义一个栈
        if k==len(num):
            return '0'
        stack = []
        for i in num:
            while k and stack and stack[-1] >i:
                stack.pop()
                k-=1
            stack.append(i)
        while k!=0:
            stack.pop()
            k-=1
        return ''.join(a)

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        te = temp
        Number = temp.val
        temp = temp.next
        while temp!=None:
            if temp.val == Number:
                te.next=temp.next
                temp = temp.next
                #Number = temp.val
            else:
                Number = temp.val
                te = temp
                temp=temp.next
        return head

if __name__ == '__main__':
    test = Solution()
    print(test.removeKdigits("112",1))
