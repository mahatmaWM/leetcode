#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (73.43%)
# Likes:    566
# Dislikes: 0
# Total Accepted:    188.4K
# Total Submissions: 256.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最大深度 3 。
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
    # 深度为根节点到最远叶子节点的最长路径上的节点数
    def maxDepth(self, root: TreeNode) -> int:

        def helper(node):
            if not node: return 0
            if node.left and not node.right:
                return 1 + helper(node.left)
            elif node.right and not node.left:
                return 1 + helper(node.right)
            else:
                return 1 + max(helper(node.left), helper(node.right))

        return helper(root)
# @lc code=end
