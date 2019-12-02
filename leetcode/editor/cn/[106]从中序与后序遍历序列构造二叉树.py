# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意: 
# 你可以假设树中没有重复的元素。
#
# 例如，给出 
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
# 返回如下的二叉树： 
#
#     3
#   / \
#  9  20
#    /  \
#   15   7
# 
# Related Topics 树 深度优先搜索 数组

# 因为后序遍历最后遍历根节点，所以postorder的最后一个元素就是根节点(postorder [-1])，因为中序遍历先遍历左半部分，再遍历根节点，
# 所以inorder 中postorder [-1]的位置 index 左侧的元素inorder [:index]构成二叉树的左子树， index位置 右侧的元素inorder [index+1:]构成二叉树的右子树
# 在postorder 中,postorder [：index]构成二叉树的左子树，postorder [index：-1]构成二叉树的右子树，postorder [index-1]为左子树的根节点，postorder [-2]为右子树的根节点，
# 先利postorder [：index]，inorder [:index]构造左子树，再用postorder [index：-1]和inorder [index+1:]构造右子树，用递归即可


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None

        i = inorder.index(postorder[-1])
        N = TreeNode(postorder[-1])
        N.left = self.buildTree(inorder[:i], postorder[:i])
        N.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return N

# leetcode submit region end(Prohibit modification and deletion)
