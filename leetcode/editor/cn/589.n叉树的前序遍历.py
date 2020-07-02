#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (73.23%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    31.9K
# Total Submissions: 43.4K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的前序遍历。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其前序遍历: [1,3,5,6,2,4]。
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
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        def helper(node):
            if not node: return
            self.res.append(node.val)
            for child in node.children:
                helper(child)
        helper(root)
        return self.res

# @lc code=end

