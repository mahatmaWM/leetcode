#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (50.37%)
# Likes:    378
# Dislikes: 0
# Total Accepted:    53.2K
# Total Submissions: 105.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
# 示例 :
# 给定二叉树
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
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

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        max_path_length = 0

        # 求树的深度
        def tree_depth(node):
            nonlocal max_path_length
            if not node: return 0
            left_depth, right_depth = 0, 0
            if node.left: left_depth = tree_depth(node.left)
            if node.right: right_depth = tree_depth(node.right)
            # 经过结点node的最长路径，等与它左子树的深度 + 右子树的深度
            max_path_length = max(max_path_length, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        tree_depth(root)
        return max_path_length


# @lc code=end
