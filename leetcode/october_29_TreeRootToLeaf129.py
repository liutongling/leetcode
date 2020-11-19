#给定一个二叉树，它的每个结点都存放一个 0-9 的数字，
# 每条从根到叶子节点的路径都代表一个数字。
class TreeNode:
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None
class Solution:
    sumNumber = 0
    def sumNumbers(self,root: TreeNode)->int:

        if root.right==None and root.left==None:
            self.sumNumber = root.x+self.sumNumber
        else:
            pass
#这个题不会做