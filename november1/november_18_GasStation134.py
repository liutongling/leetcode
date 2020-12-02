import queue
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        longGas = len(gas)
        for i in range(longGas):
            temp = 0
            judge = 0
            for j in range(i,i+len(gas)):
                if j>=len(gas):
                    j = j-len(gas)
                if temp+gas[j]-cost[j]>=0:
                    judge+=1
                    temp = temp + gas[j]-cost[j]
                else:
                    break
            if temp>=0 and (judge==len(gas)):
                return i
        return -1
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        vist1 = deque([])
        vist2 = deque([])
        if not q and not p:
            return True
        if q == None and p != None or q != None and p == None:
            return False
        vist1.append(p)
        vist2.append(q)
        while vist2 and vist1:
            one = vist1.popleft()
            two = vist2.popleft()
            if one.val != two.val:
                return False
            else:
                if one.left and two.left:
                    vist1.append(one.left)
                    vist2.append(two.left)
                elif not one.left and not two.left:
                    pass
                else:
                    return False
                if one.right and two.right:
                    vist1.append(one.right)
                    vist2.append(two.right)
                elif not one.right and not two.right:
                    pass
                else:
                    return False
        return True

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s = s.lower()
        up = 0
        down = len(s)-1
        while up < down:
            if not(s[up].isdigit()) and (not s[up].isalpha()):
                up+=1
                continue
            if not(s[down].isdigit()) and (not s[down].isalpha()):
                down-=1
                continue
            if s[up] == s[down]:
                up+=1
                down-=1
            else:
                return False
        return True


if __name__ == '__main__':
    e = Solution()
    print(e.isPalindrome("0P"))