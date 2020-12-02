from collections import defaultdict
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lengthA = len(a)-1
        lengthB = len(b)-1
        newBinary = 0
        temp = 0
        strpre = ""
        while lengthA>=0 and lengthB>=0:
            if int(a[lengthA])+int(b[lengthB])+temp==1:
                newBinary = newBinary+1
                temp = 0
                lengthA-=1
                lengthB-=1
            elif int(a[lengthA])+int(b[lengthB])+temp==2:
                newBinary = newBinary+0
                if newBinary == 0:
                    strpre = strpre+"0"
                temp = 1
                lengthA -= 1
                lengthB -= 1
            elif int(a[lengthA])+int(b[lengthB])+temp==0:
                newBinary = newBinary + 0
                if newBinary == 0:
                    strpre = strpre+"0"
                lengthA -= 1
                lengthB -= 1
            else:
                newBinary = newBinary+1
                temp = 1
                lengthA -= 1
                lengthB -= 1

            newBinary = newBinary*10
        while lengthA>=0:
            if int(a[lengthA])+temp==1:
                newBinary = newBinary + 1
                temp = 0
                lengthA -= 1
                lengthB -= 1
            elif int(a[lengthA])+temp==2:
                newBinary = newBinary + 0
                if newBinary == 0:
                    strpre = strpre+"0"
                temp = 1
                lengthA -= 1
            else:
                newBinary = newBinary + 0
                if newBinary == 0:
                    strpre = strpre + "0"
                temp = 0
                lengthA -= 1
            # else:
            #     newBinary = newBinary+0
            #     temp= 1
            #     lengthA -= 1
            #     lengthB -= 1
            newBinary*=10
        while lengthB>=0:
            if int(b[lengthB])+temp==1:
                newBinary = newBinary + 1
                temp = 0
                lengthA -= 1
                lengthB -= 1
            elif int(b[lengthB])+temp==0:
                newBinary = newBinary + 0
                if newBinary == 0:
                    strpre = strpre + "0"
                temp = 0
                lengthB-=1
            else:
                newBinary = newBinary+0
                if newBinary == 0:
                    strpre = strpre+"0"
                temp= 1
                lengthB -= 1
            newBinary*=10
        newBinary = newBinary+temp
        if newBinary%10 == 0:
            newBinary = newBinary//10
        if newBinary == 0:
            return '0'
        testStr = strpre+str(newBinary)
        return testStr[::-1]

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        result1=[]
        result2=[]
        te = TreeNode()
        te.val=0
        if not q and not p:
            return True
        if q==None and p!=None or q!=None and p==None:
            return False
        queueq = deque([q])
        while queueq:
            node = queueq.popleft()
            result1.append(node.val)
            if node.left:
                queueq.append(node.left)

            if node.right:
                queueq.append(node.right)

        queuep = deque([p])
        while queuep:
            node = queuep.popleft()
            result2.append(node.val)
            if node.left:
                queuep.append(node.left)

            if node.right:
                queuep.append(node.right)

        if result1==result2:
            return True
        else:
            return False

if __name__ == '__main__':
    test = Solution()
    te = test.addBinary("100","110010")
    print(te)