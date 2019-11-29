# 给定一个二叉树，返回它的 前序 遍历。
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
# 输出: [1,2,3]
# 
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
# Related Topics 栈 树

# 递归版本：
# def preOrder(sellf, root):
#     if root == None:
#         return
#     print(root.val)
#     self.preOrder(root.left)
#     self.preOrder(root.right)

# 非递归版本：
# 使用栈来实现
# 每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点，再访问其右子树。


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

# leetcode submit region end(Prohibit modification and deletion)
