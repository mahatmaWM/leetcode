#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (46.69%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 27.3K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或
# 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
#
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
#
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
#
#
# 示例 2:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 2   2
#
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。
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
    # 此二叉树比较特殊，其父节点的值会小于子节点的值，每个节点的子节点数量只能为 2 或 0
    #
    # 思路：根据定义，根节点的值肯定是二叉树中最小的值，剩下的只需要找到左右子树中比跟节点大的最小值就可以了。
    # 这里先序遍历二叉树，对于当前节点，如果大于整颗树的root节点值大，则存起来。
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = float('inf')

        def traverse(node):
            nonlocal res
            if not node: return
            if root.val < node.val < res: res = node.val
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return -1 if res == float('inf') else res


# @lc code=end
