#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#
# https://leetcode-cn.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (55.36%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 23.9K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，计算整个树的坡度。
#
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
#
# 整个树的坡度就是其所有节点的坡度之和。
#
#
#
# 示例：
#
# 输入：
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# 输出：1
# 解释：
# 结点 2 的坡度: 0
# 结点 3 的坡度: 0
# 结点 1 的坡度: |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
#
#
#
#
# 提示：
#
#
# 任何子树的结点的和不会超过 32 位整数的范围。
# 坡度的值不会超过 32 位整数的范围。
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

    def findTilt1(self, root: TreeNode) -> int:
        # 返回的tuple为(子树和，坡度和)
        def dfs(node):
            if not node: return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            return node.val + left[0] + right[0], abs(left[0] - right[0]) + left[1] + right[1]

        return dfs(root)[1]

    def findTilt(self, root: TreeNode) -> int:
        self.res = 0

        # 返回的子树和
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res += abs(left - right)
            return node.val + left + right

        dfs(root)
        return self.res


# @lc code=end
