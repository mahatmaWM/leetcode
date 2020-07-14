#
# @lc app=leetcode.cn id=1145 lang=python3
#
# [1145] 二叉树着色游戏
#
# https://leetcode-cn.com/problems/binary-tree-coloring-game/description/
#
# algorithms
# Medium (42.54%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 8.3K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10,11]\n11\n3'
#
# 有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到
# n 各不相同。
#
#
#
# 游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，
#
# 「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）；
#
# 「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。
#
# 「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。
#
#
#
# 之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。
#
# 如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。
#
# 若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。
#
#
#
# 现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true；若无法获胜，就请返回 false。
#
#
#
# 示例：
#
#
#
# 输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# 输出：True
# 解释：第二个玩家可以选择值为 2 的节点。
#
#
#
#
# 提示：
#
#
# 二叉树的根节点为 root，树上由 n 个节点，节点上的值从 1 到 n 各不相同。
# n 为奇数。
# 1 <= x <= n <= 100
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
    # 思路：如果第一个用户选择了x节点，整棵树会被分成3个部分{x节点的左孩子、x节点的右孩子、其他部分}
    # 分别设为A B C 三部分，统计各个部分的大小，就能确定第二个用户如何选择（统计大小可以dfs后序遍历树计数）
    # dfs遍历树，既可以找到A B两部分的大小
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        red_left, red_right = 0, 0

        def dfs(root):
            nonlocal red_left, red_right
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == x:
                red_left = left
                red_right = right
            return left + right + 1

        dfs(root)
        other = n - red_left - red_right - 1
        choice = [other, red_left, red_right]
        return max(choice) > n - max(choice)


# @lc code=end
