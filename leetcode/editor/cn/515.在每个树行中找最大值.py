#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (60.44%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    12.6K
# Total Submissions: 20.8K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
#
# 示例：
#
#
# 输入:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# 输出: [1, 3, 9]
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

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        cur, res = [root], []
        while cur:
            layer = []
            layer_max = float('-inf')
            for node in cur:
                layer_max = max(layer_max, node.val)
                if node.left: layer.append(node.left)
                if node.right: layer.append(node.right)
            cur = layer
            res.append(layer_max)
        return res


# @lc code=end
