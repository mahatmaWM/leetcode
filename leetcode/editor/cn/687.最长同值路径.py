#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# https://leetcode-cn.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (40.50%)
# Likes:    281
# Dislikes: 0
# Total Accepted:    17.8K
# Total Submissions: 43.9K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。
#
# 示例 1:
#
# 输入:
#
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
# 输出:
#
#
# 2
#
#
# 示例 2:
#
# 输入:
#
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
# 输出:
#
#
# 2
#
#
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
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
    # 最长路径只有可能是两种情况：1、节点node往一个分支走到某一个位置的一条路径。2、节点node两边可走，最长路径等于两边之和。
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 后序遍历二叉树
        # dfs(node, val)，返回node节点为根的最长路径 和 val值往下走的最大长度
        def dfs(node, val):
            if not node: return 0, 0
            left_max_path, left_max_val = dfs(node.left, node.val)
            right_max_path, right_max_val = dfs(node.right, node.val)

            curr_max_path = max(left_max_path, right_max_path, left_max_val + right_max_val)
            if node.val != val:
                return curr_max_path, 0
            else:
                return curr_max_path, max(left_max_val, right_max_val) + 1

        if not root: return 0
        return dfs(root, root.val)[0]


# @lc code=end
