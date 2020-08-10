#
# @lc app=leetcode.cn id=655 lang=python3
#
# [655] 输出二叉树
#
# https://leetcode-cn.com/problems/print-binary-tree/description/
#
# algorithms
# Medium (56.74%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 7.2K
# Testcase Example:  '[1,2]'
#
# 在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：
#
#
# 行数 m 应当等于给定二叉树的高度。
# 列数 n 应当总是奇数。
#
# 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
# 每个未使用的空间应包含一个空的字符串""。
# 使用相同的规则输出子树。
#
#
# 示例 1:
#
#
# 输入:
# ⁠    1
# ⁠   /
# ⁠  2
# 输出:
# [["", "1", ""],
# ⁠["2", "", ""]]
#
#
# 示例 2:
#
#
# 输入:
# ⁠    1
# ⁠   / \
# ⁠  2   3
# ⁠   \
# ⁠    4
# 输出:
# [["", "", "", "1", "", "", ""],
# ⁠["", "2", "", "", "", "3", ""],
# ⁠["", "", "4", "", "", "", ""]]
#
#
# 示例 3:
#
#
# 输入:
# ⁠     1
# ⁠    / \
# ⁠   2   5
# ⁠  /
# ⁠ 3
# ⁠/
# 4
# 输出:
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
# ⁠["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
# ⁠["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
# ⁠["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
#
#
# 注意: 二叉树的高度在范围 [1, 10] 中。
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

    def printTree(self, root: TreeNode) -> List[List[str]]:

        def maxDepth(node):
            if not node: return 0
            return max(maxDepth(node.left), maxDepth(node.right)) + 1

        def helper(depth, root, index):
            if not root: return
            order.append((depth, root.val, index))
            helper(depth + 1, root.left, 2 * index)
            helper(depth + 1, root.right, 2 * index + 1)
            return

        if not root: return [[""]]
        max_depth = maxDepth(root)
        m, n = (max_depth), (2**(max_depth) - 1)
        res = [[""] * n for i in range(m)]

        # 前序遍历，把每个节点的(深度，值，索引)找出来
        order = []
        helper(0, root, 0)
        for d, v, i in order:
            # 把树中的索引转化为矩阵中的索引
            i_new = int(((n + 1) / (2**(d + 1))) * (2 * i + 1) - 1)
            res[d][i_new] = str(v)
        return res


# @lc code=end
