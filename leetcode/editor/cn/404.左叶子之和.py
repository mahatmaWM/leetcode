# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#
#
# Related Topics 树

# 前序遍历二叉树，遇到左叶子就计数（问题就变成如何判断左叶子）

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def traverse(node):
            if not node: return
            # 判断左叶子
            if node.left and node.left.left is None and node.left.right is None:
                self.res += node.left.val
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
