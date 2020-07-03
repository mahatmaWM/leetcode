#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (49.31%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    23.5K
# Total Submissions: 47.3K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# 给定一个二叉树
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
# 进阶：
#
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#
#
#
# 示例：
#
#
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#
#
#
# 提示：
#
#
# 树中的节点数小于 6000
# -100 <= node.val <= 100
#
#
#
#
#
#
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # 层次遍历，获得每一层节点的list然后对每一个list的next进行赋值
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_level.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            # 连接当前层
            for i in range(len(curr_level) - 1):
                curr_level[i].next = curr_level[i + 1]
        return root

# @lc code=end

