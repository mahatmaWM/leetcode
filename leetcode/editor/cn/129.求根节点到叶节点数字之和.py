#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        res = 0

        def helper(node, curr_res):
            nonlocal res
            if not node: return
            curr_res = 10 * curr_res + node.val
            if not node.left and not node.right: res += curr_res
            helper(node.left, curr_res)
            helper(node.right, curr_res)

        helper(root, 0)
        return res


# @lc code=end
