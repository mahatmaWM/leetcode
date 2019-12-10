# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征： 
#
# 
# 节点的左子树只包含小于当前节点的数。 
# 节点的右子树只包含大于当前节点的数。 
# 所有左子树和右子树自身必须也是二叉搜索树。 
# 
#
# 示例 1: 
#
# 输入:
#    2
#   / \
#  1   3
# 输出: true
# 
#
# 示例 2: 
#
# 输入:
#    5
#   / \
#  1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
# 
# Related Topics 树 深度优先搜索

# 思路：中序遍历递增 则为搜索二叉树

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.in_order(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def in_order(self, root, res):
        if root:
            self.in_order(root.left, res)
            res.append(root.val)
            self.in_order(root.right, res)

    # def is_val(self, node):
    #     if node is None:
    #         return True
    #     if node.left is not None and node.left.val >= node.val:
    #         return False
    #
    #     if node.right is not None and node.right.val <= node.val:
    #         return False
    #
    #     return self.is_val(node.left) and self.is_val(node.right)
    #
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     return True if root is None else self.is_val(root)

    # def is_val(self, node, min_v, max_v):
    #     if node is None:
    #         return True
    #     if node.left is not None:
    #         if node.left.val >= node.val or node.left.val <= min_v:
    #             return False
    #
    #     if node.right != None:
    #         if node.right.val <= node.val or node.right.val >= max_v:
    #             return False
    #
    #     return self.is_val(node.left, min_v, node.val) and self.is_val(
    #         node.right, node.val, max_v)
    #
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     return True if root is None else self.is_val(root, -(2 ** 32), 2 ** 32)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    print(Solution().isValidBST(root=root))
