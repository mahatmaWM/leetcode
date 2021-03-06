#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (54.71%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 50.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
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
    # 前序遍历二叉树，遇到左叶子就计数（问题就变成如何判断左叶子）
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0

        def traverse(node):
            nonlocal res
            if not node: return
            # 判断左叶子
            if node.left and not node.left.left and not node.left.right: res += node.left.val
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return res

# @lc code=end

