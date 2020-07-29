#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#
# https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (48.39%)
# Likes:    60
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 13.2K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给定一个二叉树，确定它是否是一个完全二叉树。
#
# 百度百科中对完全二叉树的定义如下：
#
# 若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h
# 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2^h 个节点。）
#
#
#
# 示例 1：
#
#
#
# 输入：[1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
#
#
# 示例 2：
#
#
#
# 输入：[1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的结点没有尽可能靠向左侧。
#
#
#
#
# 提示：
#
#
# 树中将会有 1 到 100 个结点。
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


import collections


class Solution:
    # 层次遍历树
    # 如果当前层遇到一个空节点时，下一层 或者 当前层剩余中 还有非None节点，则不满足
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque()
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
            # 如果遇到一个空节点，查看queue是否包含非None的节点
            elif any(queue):
                return False
        return True


# @lc code=end
