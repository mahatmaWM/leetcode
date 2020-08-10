#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (65.81%)
# Likes:    280
# Dislikes: 0
# Total Accepted:    116K
# Total Submissions: 176.2K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# 输出: [1,2,3]
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def preOrder(node):
            nonlocal res
            if not node: return
            res.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return res


class Solution:
    # 非递归版本：使用栈来实现
    # 每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点，再访问其右子树。
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = []
        node = root
        while node or stack:
            # 一直处理完左边节点
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            # 指向右孩子
            node = stack.pop()
            node = node.right
        return res


# @lc code=end
