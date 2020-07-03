#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#
# https://leetcode-cn.com/problems/trim-a-binary-search-tree/description/
#
# algorithms
# Easy (65.85%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    13.8K
# Total Submissions: 20.9K
# Testcase Example:  '[1,0,2]\n1\n2'
#
# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L)
# 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
#
# 示例 1:
#
#
# 输入:
# ⁠   1
# ⁠  / \
# ⁠ 0   2
#
# ⁠ L = 1
# ⁠ R = 2
#
# 输出:
# ⁠   1
# ⁠     \
# ⁠      2
#
#
# 示例 2:
#
#
# 输入:
# ⁠   3
# ⁠  / \
# ⁠ 0   4
# ⁠  \
# ⁠   2
# ⁠  /
# ⁠ 1
#
# ⁠ L = 1
# ⁠ R = 3
#
# 输出:
# ⁠     3
# ⁠    /
# ⁠  2
# ⁠ /
# ⁠1
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
    # 给定一棵二叉排序树，[L R]，让你把树中低于最小值和高于最大值的数删了，并返回此时树的根节点。
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        # 当 node.val>R 时，继续修剪节点左侧，右子树一定比R大。
        # 当 node.val<L 时，继续修剪节点右侧，左子树一定比L小。
        # 否则，我们修剪树的两边。
        def trim(node):
            if not node: return None
            if node.val > R: return trim(node.left)
            if node.val < L: return trim(node.right)

            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

        return trim(root)


# @lc code=end
