#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (71.72%)
# Likes:    531
# Dislikes: 0
# Total Accepted:    172.1K
# Total Submissions: 239.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
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
    # 递归的版本
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def inOrder(root):
            if not root: return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return res

class Solution:
    # 非递归版本：中序遍历是先入栈，然后节点弹出栈后再访问。
    def inorderTraversal(self, root):
        if not root: return []
        res = []
        stack = []
        node = root
        while node or stack:
            # 一直找左边的节点
            while node:
                stack.append(node)
                node = node.left

            # 没有左边节点了
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
# @lc code=end
