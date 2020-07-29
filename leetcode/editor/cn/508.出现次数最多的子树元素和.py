#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#
# https://leetcode-cn.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (64.47%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    6.6K
# Total Submissions: 10.2K
# Testcase Example:  '[5,2,-3]'
#
# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
#
# 你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
#
#
#
# 示例 1：
# 输入:
#
# ⁠ 5
# ⁠/  \
# 2   -3
#
#
# 返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
#
# 示例 2：
# 输入：
#
# ⁠ 5
# ⁠/  \
# 2   -5
#
#
# 返回 [2]，只有 2 出现两次，-5 只出现 1 次。
#
#
#
# 提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
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
    # 递归遍历树，保存子树和于hashmap，最后遍历hashmap找出现最大次数的元素和
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []
        import collections
        hashmap = collections.defaultdict(int)

        # 返回node节点的子树元素和
        def helper(node):
            if not node: return 0
            nonlocal hashmap
            node_sum = helper(node.left) + helper(node.right) + node.val
            hashmap[node_sum] += 1
            return node_sum

        helper(root)

        ans = []
        max_cnt = 0
        for key, val in hashmap.items():
            if val == max_cnt:
                ans.append(key)
            elif val > max_cnt:
                max_cnt = val
                ans = [key]
        return ans


# @lc code=end
