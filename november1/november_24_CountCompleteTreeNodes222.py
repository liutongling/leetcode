from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#使用广度遍历（bfs）
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        #判断如果根节点是空
        if not root:
            return 0
        #定义一个队列
        queue =  deque([root])
        count = 1
        while queue:
            childen = queue.popleft()
            if childen.left:
                queue.append(childen.left)
                count+=1
            if childen.right:
                queue.append(childen.right)
                count+=1
        return count
    def dfs(self,root:TreeNode)->int:
