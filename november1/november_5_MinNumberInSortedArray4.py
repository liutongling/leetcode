from collections import defaultdict
from collections import deque
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        longNumber = len(nums2)+len(nums1)
        if longNumber%2==0:
            index1 = longNumber//2
            index2 = index1+1
        else:
            index1 = longNumber//2+1

        #保存数值
        count1 = 0
        count2 = 0
        if longNumber%2 == 0:
            pre1 = 0
            pre2 = 0
            count = 0
            while pre1<len(nums1) and pre2<len(nums2):
                if nums1[pre1] < nums2[pre2]:
                    count+=1
                    if count == index1:
                        count1 = nums1[pre1]
                    elif count == index2:
                        count2 = nums1[pre1]
                    pre1+=1
                else:
                    count+=1
                    if count == index1:
                        count1 = nums2[pre2]
                    elif count == index2:
                        count2 = nums2[pre2]
                    pre2+=1
            while pre1 < len(nums1):
                count+=1
                if count == index1:
                    count1 = nums1[pre1]
                elif count == index2:
                    count2 = nums1[pre1]
                pre1 += 1
            while pre2 < len(nums2):
                count+=1
                if count == index1:
                    count1 = nums2[pre2]
                elif count == index2:
                    count2 = nums2[pre2]
                pre2 += 1
        else:
            pre1 = 0
            pre2 = 0
            count = 0
            while pre1 < len(nums1) and pre2 < len(nums2):
                if nums1[pre1] < nums2[pre2]:
                    count += 1
                    if count == index1:
                        count1 = nums1[pre1]
                    pre1 += 1
                else:
                    count += 1
                    if count == index1:
                        count1 = nums2[pre2]
                    pre2 += 1
            while pre1 < len(nums1):
                count += 1
                if count == index1:
                    count1 = nums1[pre1]
                pre1 += 1
            while pre2 < len(nums2):
                count += 1
                if count == index1:
                    count1 = nums2[pre2]
                pre2 += 1
        if longNumber % 2 == 0:
            return (count1+count2)/2
        else:
            return float(count1)

    def ladderLength(self, beginWord, endWord, wordList):
        pass

    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1 and s != " ":
            return 1
        if len(s) == 1 and s == " ":
            return 0

        list_str = s.split(" ")
        cont = -1
        while cont != -(len(list_str)+1):
            if list_str[cont] == ' ' or list_str[cont] == '':
                cont -= 1
            else:
                return len(list_str[cont])

    def plusOne(self, digits: list) -> list:
        #将数组反转
        long = len(digits)
        digits.reverse()
        res = []
        count = 0
        temp = 0
        while count < long:
            if count ==0:
                if digits[count]+1==10:
                    res.append(0)
                    temp = 1
                    count+=1
                else:
                    res.append(digits[count]+1)
                    temp = 0
                    count += 1
            else:
                if digits[count]+temp == 10:
                    temp = 1
                    res.append(0)
                    count += 1
                else:
                    res.append(digits[count] + temp)
                    temp = 0
                    count += 1
        if temp == 1:
            res.append(temp)
        res.reverse()
        return res

#python实现广度优先算法（Breadth-First-Search），简称BFS，是一种图形搜索演算算法。
#definition for a binary tree node
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
def level_order_tree(root:TreeNode,result):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

if __name__ == '__main__':
    test = Solution()
    midnumber = test.plusOne([9])
    print(midnumber)
