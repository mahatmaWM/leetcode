# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例: 
#
# 输入: 3
# 输出:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3
# 
# Related Topics 树 动态规划

# 思路：
# 因为要输出二叉搜索树，所以需要构造树。
# 依次选取每个节点作为根节点，组合其左边的树集合，右边的树集合。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def generate(start, end):
            trees = []
            for root in range(start, end):
                for left in generate(start, root):
                    for right in generate(root + 1, end):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            return trees

        return generate(1, n + 1)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().generateTrees(n=3))
