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


class Solution:
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

class Solution1(object):
    # 非递归版本：中序的非递归遍历与先序的非递归遍历类似。
    # 先序遍历是先访问节点，然后再将节点入栈，
    # 而中序遍历则是先入栈，然后节点弹出栈后再访问。
    def inorderTraversal(self, root):
        if not root: return []
        res = []
        stack = []
        node = root
        while node or stack:
            # 从根节点开始，一直找左边节点
            while node:
                stack.append(node)
                node = node.left
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res
# @lc code=end
