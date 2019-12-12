# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。 
#
# 示例 1: 
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# 
#
# 示例 2: 
#
# 输入: [3,1,4,null,null,2]
#
#  3
# / \
# 1   4
#    /
#   2
#
# 输出: [2,1,4,null,null,3]
#
#  2
# / \
# 1   4
#    /
#  3 
#
# 进阶: 
#
# 
# 使用 O(n) 空间复杂度的解法很容易实现。 
# 你能想出一个只使用常数空间的解决方案吗？ 
# 
# Related Topics 树 深度优先搜索

# 思路:
# 这道题难点,是找到那两个交换节点,把它交换过来就行了.如何找到这两个点呢？
# 这里我们二叉树搜索树的中序遍历(中序遍历遍历元素是递增的)
# 如上图示例1所示, 中序遍历顺序是 3 2 1，我们只要找到节点3和节点1交换顺序即可!
#
# 这里我们有个规律发现这两个节点:
# 第一个节点,是第一个按照中序遍历时候前一个节点大于后一个节点,我们选取前一个节点,这里指节点3;
# 第二个节点,是在第一个节点找到之后, 后面出现前一个节点大于后一个节点，我们选择后一个节点，这里指节点1;

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre_visit, self.first, self.second = None, None, None
        self.in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        # 先找到第一次出现逆序的first节点，再找到最后一次逆序的second节点
        if self.pre_visit and self.pre_visit.val > node.val:
            if not self.first:
                self.first = self.pre_visit
            self.second = node
        self.pre_visit = node
        self.in_order(node.right)

# leetcode submit region end(Prohibit modification and deletion)
