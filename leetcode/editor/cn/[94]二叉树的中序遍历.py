# 给定一个二叉树，返回它的中序 遍历。
#
# 示例: 
#
# 输入: [1,null,2,3]
#   1
#    \
#     2
#    /
#   3
#
# 输出: [1,3,2]
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
# Related Topics 栈 树 哈希表

# 递归版本：
# def inOrder(self, root):
#     if root == None:
#         return
#     self.inOrder(root.left)
#     print(root.val)
#     self.inOrder(root.right)

# 非递归版本：
# 中序的非递归遍历与先序的非递归遍历类似。
# 先序遍历是先访问节点，然后再将节点入栈，
# 而中序遍历则是先入栈，然后节点弹出栈后再访问。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        res = []
        stack = []
        node = root
        while node or stack:
            # 从根节点开始，一直找左子树
            while node:
                stack.append(node)
                node = node.left
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

# leetcode submit region end(Prohibit modification and deletion)
