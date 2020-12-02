#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level)
#将二叉树进行层遍历，每一层的数值放入列表中(力扣题目102）
#copyright:liutongling

from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#使用广度优先遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        #定义一个队列
        queue = deque([root])
        #queue1 = deque([])
        li = []
        while queue:
            #queue1.append(queue[0])
            count = len(queue)
            temp = []
            #存放删除的节点
            new1 = deque([])
            for i in range(count):
                new = queue.popleft()
                temp.append(new.val)
                new1.append(new)
            while new1:
                l = new1.popleft()
                if l.left:
                    queue.append(l.left)
                if l.right:
                    queue.append(l.right)
            li.append(temp)
        return li
if __name__ == '__main__':
    root = TreeNode(3)
    left = TreeNode(9)
    right = TreeNode(20)
    root.left = left
    root.right = right
    t = Solution()
    li = t.levelOrder(root)
    print(li)
