#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (57.21%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    19.1K
# Total Submissions: 33.3K
# Testcase Example:  '[1,3,null,null,2]'
#
# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。
#
# 示例 1:
#
# 输入: [1,3,null,null,2]
#
# 1
# /
# 3
# \
# 2
#
# 输出: [3,1,null,null,2]
#
# 3
# /
# 1
# \
# 2
#
#
# 示例 2:
#
# 输入: [3,1,4,null,null,2]
#
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
#
# 输出: [2,1,4,null,null,3]
#
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
#
# 进阶:
#
#
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# 思路：
# 二叉树搜索树的中序遍历(中序遍历遍历元素是递增的)
# 这道题难点是如何找到这两个点呢？
# 如上图示例1所示, 中序遍历顺序是 3 2 1，我们只要找到节点3和节点1交换顺序即可!
# 寻找第一个节点：中序遍历时，第一次出现前一个节点大于后一个节点，我们选取前一个节点作为first，这里指节点3
# 寻找第二个节点：找到第一个节点后，最后一次出现前一个节点大于后一个节点时，我们选择后一个节点作为second，这里指节点1
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_visit, first, second = None, None, None

        def in_order(node):
            if not node: return
            in_order(node.left)

            nonlocal pre_visit, first, second
            # 当前访问节点node，前一次访问的节点pre_visit
            # 先找到第一次出现逆序的first节点，再找到最后一次逆序的second节点
            if pre_visit and pre_visit.val > node.val:
                if not first:
                    first = pre_visit
                second = node
            pre_visit = node

            in_order(node.right)

        in_order(root)
        first.val, second.val = second.val, first.val


# @lc code=end
