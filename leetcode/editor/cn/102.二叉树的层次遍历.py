# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如: 
# 给定二叉树: [3,9,20,null,null,15,7],
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
# 
#
# 返回其层次遍历结果： 
#
# [
#  [3],
#  [9,20],
#  [15,7]
# ]
# 
# Related Topics 树 广度优先搜索

# 思路：
# 广度优先遍历是以层为顺序，将某一层上的所有节点都搜索到了之后才向下一层搜索；
# 使用队列的性质来进行层次访问。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 借助队列deque的非递归层次遍历
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        retList = []
        if root is None:
            return retList

        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            curr_level = []
            curr_level_len = len(queue)
            for _ in range(curr_level_len):
                node = queue.popleft()
                curr_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            retList.append(curr_level)
        return retList

    # 递归的方式实现层次遍历
    def levelOrder1(self, root):
        def helper(node, level):
            # 如果递归到一个新的层时
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        levels = []
        if not root:
            return levels
        helper(root, 0)
        return levels

# leetcode submit region end(Prohibit modification and deletion)
