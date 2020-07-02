#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (69.61%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 37.2K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 我们应返回其最大深度，3。
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        if not root.children: return 1
        res = 0
        for child in root.children:
            res = max(res, self.maxDepth(child) + 1)
        return res


# @lc code=end
