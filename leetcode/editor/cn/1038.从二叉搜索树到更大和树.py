#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
#
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (75.23%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 13K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# 给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
#
#
#
#
# 示例：
#
#
#
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
#
#
#
#
# 提示：
#
#
# 树中的节点数介于 1 和 100 之间。
# 每个节点的值介于 0 和 100 之间。
# 给定的树为二叉搜索树。
#
#
#
#
# 注意：该题目与 538: https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
# 相同
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
    # 右中左的方式遍历即可
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = 0

        def inorder(node):
            nonlocal sum
            if not node: return
            inorder(node.right)
            sum += node.val
            node.val = sum
            inorder(node.left)

        inorder(root)
        return root


# @lc code=end
