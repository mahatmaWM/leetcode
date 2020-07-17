#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (63.72%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    49.5K
# Total Submissions: 77.7K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    # 比较直观的做法是采用层次遍历二叉树，然后获取每一层的最右边的节点即可。
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        retList = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            retList.append(curr_level[-1])
        return retList


# @lc code=end
