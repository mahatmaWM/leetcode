#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (73.67%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    26.7K
# Total Submissions: 36.2K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的后序遍历。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其后序遍历: [5,6,3,2,4,1].
#
#
#
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
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

    def postorder(self, root: 'Node') -> List[int]:
        self.res = []

        def helper(node):
            if not node: return
            for child in node.children:
                helper(child)
            self.res.append(node.val)

        helper(root)
        return self.res


# @lc code=end
