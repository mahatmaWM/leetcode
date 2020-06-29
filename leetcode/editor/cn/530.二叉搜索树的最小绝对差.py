#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (57.17%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    16.7K
# Total Submissions: 29.1K
# Testcase Example:  '[1,null,3,2]'
#
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
#
#
#
# 示例：
#
# 输入：
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# 输出：
# 1
#
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#
#
#
#
# 提示：
#
#
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
# 相同
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

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res, self.prev = float("inf"), float("-inf")

        # 二叉搜索树中序遍历是严格有序的，在遍历的过程中记录每次current与previous的差值即可
        def in_order(root):
            if root is None: return

            in_order(root.left)
            self.res = min(self.res, abs(root.val - self.prev))
            self.prev = root.val
            in_order(root.right)
            return

        in_order(root)
        return self.res


# @lc code=end
