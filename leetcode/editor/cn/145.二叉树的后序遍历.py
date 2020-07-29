#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (71.67%)
# Likes:    326
# Dislikes: 0
# Total Accepted:    85.3K
# Total Submissions: 119.1K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    # 非递归版本：采用两个栈。
    # 处理stack1时按照左孩子、右孩子入栈，同时把根入stack2，注意这里根不用再入栈stack1！！！否则会死循环
    # 而且继续处理stack1的时候，stack2就变成了根、右孩子、左孩子。
    # 最后把stack2出栈，就相当于是左孩子、右孩子、根 的后续遍历结果。
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack1 = []
        stack2 = []

        stack1.append(root)
        # 这个while循环用户找到后续遍历的逆序，存在stack2中
        while stack1:
            node = stack1.pop()
            if node.left: stack1.append(node.left)
            if node.right: stack1.append(node.right)
            stack2.append(node)

        while stack2:
            res.append(stack2.pop().val)
        return res


class Solution1:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def postOrder(root):
            nonlocal res
            if not root: return
            postOrder(root.left)
            postOrder(root.right)
            res.append(root.val)

        postOrder(root)
        return res


# @lc code=end
