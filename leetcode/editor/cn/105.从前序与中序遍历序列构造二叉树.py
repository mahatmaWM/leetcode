# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
# 返回如下的二叉树：
#
#     3
#   / \
#  9  20
#    /  \
#   15   7
# Related Topics 树 深度优先搜索 数组

# 思路：
# 首先根据前序遍历的定义可以知道，preorder这个数组的第一个元素preorder[0]一定是root。
# 再根据中序遍历的定义，在inorder这个数组里，root前面的元素都属于root的左子树，root后面的元素都属于右子树，从这一步得到了left_inorder和right_inorder，
# 接下来我们只需要把root在inorder里的位置index = inorder.index(preorder[0])查找出来，就可以知道其左子树和右子树的长度，
# 然后再回到preorder，root后面先是左子树，然后是右子树，因为上一步我们已经知道了它们的长度，所以可以得到left_preorder和left_preorder，然后递归。


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        # 先找到root节点 和 左右子树的范围，然后类似前序遍历的方式构造树
        root = TreeNode(preorder[0])
        left_inorder = inorder[: inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val) + 1:]

        l_left = len(left_inorder)
        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

# leetcode submit region end(Prohibit modification and deletion)
