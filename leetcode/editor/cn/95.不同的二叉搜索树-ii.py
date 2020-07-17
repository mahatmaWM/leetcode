#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (62.98%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    33K
# Total Submissions: 52.4K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
#
#
#
# 示例：
#
# 输入：3
# 输出：
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释：
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
#
# 提示：
#
#
# 0 <= n <= 8
#
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
    # 思路：因为要输出二叉搜索树，所以需要构造树。
    # 依次选取每个节点作为根节点，组合其左边的树集合，右边的树集合。
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []

        # 类似后续遍历方式, end取n+1
        def generate(start, end):
            if start == end: return [None,]
            trees = []
            for root in range(start, end):
                for left in generate(start, root):
                    for right in generate(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            return trees

        return generate(1, n + 1)


# @lc code=end
