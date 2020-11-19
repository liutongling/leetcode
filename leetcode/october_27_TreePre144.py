#二叉树的前序遍历
#定义一个节点
#使用递归方法将，主要思想是：先判断每一个节点是否为空，
# 若不为空，将节点的值进行添加到列表中，然后将节点中的左右节点进行递归
# 若为空则返回
#
class TreeNode:
    def __init__(self,val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.list_nums = []
    def numPoint(self,point:TreeNode):
        if not root:
            return None
        self.list_nums.append(point.val)
        self.numPoint(point.left)
        self.numPoint(point.right)
    def preorderTraversal(self,root:TreeNode)->list:
        temp_root = root
        self.numPoint(temp_root)
        return self.list_nums