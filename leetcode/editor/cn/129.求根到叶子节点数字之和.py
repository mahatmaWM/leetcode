#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (63.81%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 45.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例 1:
#
# 输入: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
#
# 示例 2:
#
# 输入: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
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
    # 当访问到某一个节点时，需要把当前得到的数字传递给左右子节点。直到访问到叶子节点一个数字结束。
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        # 前序遍历二叉树，
        def dfs(node, pre_num):
            nonlocal res
            if not node: return
            pre_num = pre_num * 10 + node.val
            if not node.left and not node.right:
                res += pre_num
                return
            dfs(node.left, pre_num)
            dfs(node.right, pre_num)

        dfs(root, 0)
        return res
# @lc code=end

