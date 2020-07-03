#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (69.14%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    45.2K
# Total Submissions: 65.5K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
#
#
#
# 例如，给定二叉树
#
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
#
# 将其展开为：
#
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    # 解题思路: 递归操作
    # 1、把左子树转换成链表, 返回头结点l
    # 2、把右子树转换成链表, 返回头结点r
    # 3、把l接到root的右子树.左子树置为None
    # 4、从root开始遍历到链表尾部,把r接到链表尾部
    # 5、返回root节点
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        l = self.flatten(root.left)
        r = self.flatten(root.right)

        root.right = l
        root.left = None

        tmp = root
        while tmp.right:
            tmp = tmp.right
        tmp.right = r

        return root


# @lc code=end
