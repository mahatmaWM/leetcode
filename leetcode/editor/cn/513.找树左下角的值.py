#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#
# https://leetcode-cn.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (70.24%)
# Likes:    90
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 22.1K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，在树的最后一行找到最左边的值。
#
# 示例 1:
#
#
# 输入:
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# 输出:
# 1
#
#
#
#
# 示例 2:
#
#
# 输入:
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
#
# 输出:
# 7
#
#
#
#
# 注意: 您可以假设树（即给定的根节点）不为 NULL。
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# DFS遍历树，记录每次的树高，最大树高对应的节点即为树的最左节点。
# DFS深度递归遍历，时间O(n) 空间O(h)，h为数的高度
class Solution:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.maxdepth, self.res = -1, 0

        def dfs(root, depth):
            if not root: return
            if depth > self.maxdepth:
                self.maxdepth = depth
                self.res = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return self.res


# BFS广度循环遍历，时间O(n) 空间O(b)，b为树的宽度
class Solution1:

    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root: return []
        cur, res = [root], None
        while cur:
            layer, res = [], cur[0].val
            for node in cur:
                if node.left: layer.append(node.left)
                if node.right: layer.append(node.right)
            cur = layer
        return res


# @lc code=end
