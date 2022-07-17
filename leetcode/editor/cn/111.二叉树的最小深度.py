#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (42.61%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    85.4K
# Total Submissions: 200K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最小深度  2.
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
    # 和104题最大深度类似，
    # 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    def minDepth(self, root: TreeNode) -> int:
        # 中序遍历二叉树，
        # 如果当前节点没有左孩子，那么最小深度就是右子树最小深度+1
        # 否则就是左子树最小深度+1
        # 最后返回左右最新深度+1

        def helper(node):
            if not node: return 0

            if node.left and not node.right:
                return 1 + helper(node.left)
            elif node.right and not node.left:
                return 1 + helper(node.right)
            else:
                return 1 + min(helper(node.left), helper(node.right))

        return helper(root)

# @lc code=end
