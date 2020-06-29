#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#
# https://leetcode-cn.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (53.83%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    8.7K
# Total Submissions: 16.1K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
#
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
#
# 示例 1：
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
#
#
# 下面是两个重复的子树：
#
# ⁠     2
# ⁠    /
# ⁠   4
#
#
# 和
#
# ⁠   4
#
#
# 因此，你需要以列表的形式返回上述重复子树的根结点。
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = collections.Counter()
        ans = []

        # 递归序列化各个子树，然后检查重复出现的
        def serialize(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        serialize(root)
        return ans


# @lc code=end
