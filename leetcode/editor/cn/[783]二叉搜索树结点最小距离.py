# 给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。
#
# 示例： 
#
# 
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
#          4
#        /   \
#      2      6
#     / \    
#    1   3  
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
# 注意： 
#
# 
# 二叉树的大小范围在 2 到 100。 
# 二叉树总是有效的，每个节点的值都是整数，且不重复。 
# 
# Related Topics 树 递归

# 思路：
# 根据二叉搜索树的性质，差的绝对值一定出现在 根与左孩子 或者 根与右孩子 之间。
# 遍历过程中记录每次访问节点 与 前一次访问的节点的差值。
# 这里用中序遍历一下树。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float("inf")
        self.prev = None

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            if self.prev:
                self.res = min(self.res, node.val - self.prev.val)
            self.prev = node
            in_order(node.right)

        in_order(root)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
