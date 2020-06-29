#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (55.34%)
# Likes:    147
# Dislikes: 0
# Total Accepted:    17.2K
# Total Submissions: 31.1K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
# 案例 1:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# 输出: True
#
#
#
#
# 案例 2:
#
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# 输出: False
#
#
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
# 中序遍历bst，得到升序数组，然后二分查找是否存在目标数对（这里用n2的方法查找）
class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []

        def inOrder(root):
            if not root: return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        for i, ele in enumerate(res):
            if k - ele in res and res.index(k - ele) != i:
                return True
        return False


# @lc code=end
