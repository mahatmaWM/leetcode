#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode-cn.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (59.84%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    52.4K
# Total Submissions: 87.5K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
# 返回:
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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

    def pathSum(self, root: TreeNode, num: int) -> List[List[int]]:
        if not root: return []
        import copy
        res = []

        # 遍历的过程将路径记录下即可
        def helper(node, curr_path):
            nonlocal num
            if not node: return
            if not node.left and not node.right and sum(curr_path) + node.val == num:
                curr_path.append(node.val)
                res.append(copy.deepcopy(curr_path))
                curr_path.pop()
                return
            curr_path.append(node.val)
            if node.left:
                helper(node.left, curr_path)
            if node.right:
                helper(node.right, curr_path)
            curr_path.pop()

        helper(root, [])
        return res
# @lc code=end
