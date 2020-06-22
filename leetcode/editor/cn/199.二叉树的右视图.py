# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例: 
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#   1            <---
# /   \
# 2     3         <---
# \     \
#  5     4       <---
# 
# Related Topics 树 深度优先搜索 广度优先搜索

# 比较直观的做法是采用层次遍历二叉树，然后获取每一层的最右边的节点即可。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        retList = []
        if root is None:
            return retList

        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr_level = []
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            retList.append(curr_level[-1])
        return retList

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(Solution().rightSideView(root=root))
