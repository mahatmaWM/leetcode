# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#    1
#   / \
#  2   2
# / \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#    1
#   / \
#  2   2
#   \   \
#   3    3
#
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# Related Topics 树 深度优先搜索 广度优先搜索

# 思路：
# 判断p q两节点为根的树是否对称
#   如果都为none，则对称；如果只有一个节点为none，则不对称；
#   如果都有val，则val不同的话一定不对称；val相同，则比较p的左孩子与q的右孩子&p的右孩子和q的左孩子


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 类似先序遍历树，依次对比对称位置的两个节点
        def check(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            else:
                if p.val != q.val:
                    return False
                else:
                    return check(p.left, q.right) and check(p.right, q.left)

        if root is None: return True
        return check(root.left, root.right)

# leetcode submit region end(Prohibit modification and deletion)
