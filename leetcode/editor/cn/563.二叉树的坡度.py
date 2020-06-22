# 给定一个二叉树，计算整个树的坡度。
#
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。 
#
# 整个树的坡度就是其所有节点的坡度之和。 
#
# 示例: 
#
# 
# 输入:
#         1
#       /   \
#      2     3
# 输出: 1
# 解释:
# 结点的坡度 2 : 0
# 结点的坡度 3 : 0
# 结点的坡度 1 : |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
# 
#
# 注意: 
#
# 
# 任何子树的结点的和不会超过32位整数的范围。 
# 坡度的值不会超过32位整数的范围。 
# 
# Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Tilt = []

        # 计算每个节点的坡度，同时计算子树节点之和
        def dfs(node):
            if not node.left and not node.right:
                Tilt.append(0)
                return node.val
            if not node.left and node.right:
                right_sum = dfs(node.right)
                Tilt.append(abs(right_sum))
                return node.val + right_sum
            if node.left and not node.right:
                left_sum = dfs(node.left)
                Tilt.append(abs(left_sum))
                return node.val + left_sum
            if node.left and node.right:
                left_sum = dfs(node.left)
                right_sum = dfs(node.right)
                Tilt.append(abs(left_sum - right_sum))
                return node.val + left_sum + right_sum

        if not root:
            return 0
        dfs(root)
        return sum(Tilt)

        # # 返回的tuple为子树和，坡度和
        # def dfs2(node):
        #     if not node:
        #         return 0, 0
        #     left = dfs2(node.left)
        #     right = dfs2(node.right)
        #     return (node.val + left[0] + right[0],
        #             abs(left[0] - right[0]) + left[1] + right[1])
        # return dfs2(root)[1]

# leetcode submit region end(Prohibit modification and deletion)
