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
# 第一步定义递归函数
# def preOrder(sellf, root):
#     第二步的递归终止条件
#     if root == None:
#         return
#     第二步处理当前节点
#     print(root.val)
#     第二步递归子问题
#     self.preOrder(root.left)
#     self.preOrder(root.right)
#     这里只用到了递归的 递 阶段，没有 归 ，因为并没有把子问题返回的结果与当前阶段结果归起来处理。

# 非递归版本：
# 使用栈来实现
# 每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点，再访问其右子树。


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
            # 类似递归中 递 的部分，一直处理完左边节点
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            # 回溯，然后指向右孩子
            node = stack.pop()
            node = node.right

# leetcode submit region end(Prohibit modification and deletion)
