# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
#
# 示例 1: 
#
# 输入:
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 
#
# 注意： 
#
# 
# 节点值的范围在32位有符号整数范围内。 
# 
# Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        retList = []
        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            # visit one level node
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            retList.append(float(sum(level)) / len(level))
        return retList

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        return self.levelOrder(root)

# leetcode submit region end(Prohibit modification and deletion)
