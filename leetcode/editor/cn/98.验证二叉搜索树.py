#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (31.41%)
# Likes:    620
# Dislikes: 0
# Total Accepted:    128.9K
# Total Submissions: 410.6K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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

    def isValidBST(self, root: TreeNode) -> bool:

        # 判断node节点为根的二叉树是否合法
        # 仅当前节点合法且左右子树均合法时，才是合法
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if lower < node.val < upper and helper(node.left, lower, node.val) and helper(node.right, node.val, upper):
                return True
            return False

        return helper(root)


# @lc code=end
