#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (68.70%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    38.8K
# Total Submissions: 56.5K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
# 返回如下的二叉树：
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    # 因为后序遍历最后遍历根节点，所以postorder的最后一个元素就是根节点(postorder [-1])，因为中序遍历先遍历左半部分，再遍历根节点，
    # 所以inorder 中postorder [-1]的位置 index 左侧的元素inorder [:index]构成二叉树的左子树， index位置 右侧的元素inorder [index+1:]构成二叉树的右子树
    # 在postorder 中,postorder [：index]构成二叉树的左子树，postorder [index：-1]构成二叉树的右子树，postorder [index-1]为左子树的根节点，postorder [-2]为右子树的根节点，
    # 先利postorder [：index]，inorder [:index]构造左子树，再用postorder [index：-1]和inorder [index+1:]构造右子树，用递归即可
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None

        i = inorder.index(postorder[-1])
        node = TreeNode(postorder[-1])
        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return node


# @lc code=end
