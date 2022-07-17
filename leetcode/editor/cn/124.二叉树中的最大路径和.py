#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (40.48%)
# Likes:    473
# Dislikes: 0
# Total Accepted:    42.2K
# Total Submissions: 104.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
#
# 示例 1:
#
# 输入: [1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# 输出: 6
#
#
# 示例 2:
#
# 输入: [-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# 输出: 42
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')

        # 对于node节点，其左右子树分别贡献自己的最大值，则node节点相对于上一级的最大贡献为node.val+max(left, right)
        # 但是要注意左右子树贡献的路径可能和为0，这时需要舍弃特殊处理。
        def dfs(node):
            nonlocal max_sum
            if not node: return 0
            # 注意node节点的左右孩子有可能会贡献一个负值，这时需要置为0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            # 在dfs遍历的过程中，更新最后结果
            max_sum = max(max_sum, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return max_sum
# @lc code=end

