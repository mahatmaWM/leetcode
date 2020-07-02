#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (65.53%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    23.2K
# Total Submissions: 35.4K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其层序遍历:
#
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
#
#
#
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
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

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        retList = []
        if not root: return retList

        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr_level = []
            curr_level_len = len(queue)
            for _ in range(curr_level_len):
                node = queue.popleft()
                curr_level.append(node.val)
                for child in node.children:
                    queue.append(child)
            retList.append(curr_level)
        return retList


# @lc code=end
