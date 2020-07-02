#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (51.99%)
# Likes:    343
# Dislikes: 0
# Total Accepted:    80.8K
# Total Submissions: 155.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# 返回 false 。
#
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        # 后续遍历二叉树，当树平衡时，返回树高，否则返回-1
        def dfs(root):
            if not root: return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            if left_depth == -1: return -1
            if right_depth == -1: return -1
            if abs(left_depth - right_depth) <= 1:
                return 1 + max(left_depth, right_depth)
            else:
                return -1

        return dfs(root) != -1


# @lc code=end
