#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (57.28%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    32.6K
# Total Submissions: 56.9K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \
# ⁠    3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 示例 2:
#
# 输入: [3,4,5,1,3,null,1]
#
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \
# ⁠1   3   1
#
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
#
#
# 对于一个子树来说，有两种情况：
# 偷当前根节点
# 不偷当前根节点
#
# 情况1：偷当前根节点
# 由于包含了根节点，所以不能选择左右儿子节点，这种情况的最大值为：当前节点 + 左儿子情况2 + 右二子情况2
#
# 情况2：不包含根节点
# 这种情况，可以选择左儿子节点，所以有四种可能：
# 左儿子情况1 + 右儿子情况1
# 左儿子情况1 + 右儿子情况2
# 左儿子情况2 + 右儿子情况1
# 左儿子情况2 + 右儿子情况2
# 综合来说就是，max(左儿子情况1, 左儿子情况2) + max(右儿子情况1, 右儿子情况2)。

# 所以dfs的时候，每个节点都返回两种情况的值，最后取大者即可
# tuple为 (情况1包含当前节点的最大值，情况2不包含当前节点的最大值)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def rob(self, root: TreeNode) -> int:

        # 返回偷了node节点 和 不偷node节点 分别的最大值
        def dfs(node):
            if not node: return 0, 0
            left_pair = dfs(node.left)
            right_pair = dfs(node.right)
            return node.val + left_pair[1] + right_pair[1], \
                max(left_pair[0], left_pair[1]) + max(right_pair[0], right_pair[1])

        return max(dfs(root))


# @lc code=end
