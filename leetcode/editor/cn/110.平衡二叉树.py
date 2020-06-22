# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为： 
#
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。 
# 
#
# 示例 1: 
#
# 给定二叉树 [3,9,20,null,null,15,7] 
#
#    3
#   / \
#  9  20
#    /  \
#   15   7 
#
# 返回 true 。 
# 
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4] 
#
#       1
#      / \
#     2   2
#    / \
#   3   3
#  / \
# 4   4
# 
#
# 返回 false 。 
# Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root) != -1

    def dfs(self, root):
        if not root:
            return 0
        left_depth = self.dfs(root.left)
        if left_depth == -1:
            return -1
        right_depth = self.dfs(root.right)
        if right_depth == -1:
            return -1

        return (1 + max(left_depth, right_depth)
                ) if abs(left_depth - right_depth) <= 1 else -1

# leetcode submit region end(Prohibit modification and deletion)
