#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (52.40%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 11.3K
# Testcase Example:  '[2,1,3]'
#
# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
#
# 设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。
# 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
#
# 编码的字符串应尽可能紧凑。
#
# 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.res = []

        def helper1(root):
            if not root:
                self.res.append('#')
                return
            else:
                self.res.append(str(root.val))
                helper1(root.left)
                helper1(root.right)

        helper1(root)
        return ','.join(self.res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        d = iter(data.split(","))

        def helper2():
            tmp = next(d)
            if tmp == "#": return
            node = TreeNode(int(tmp))
            node.left = helper2()
            node.right = helper2()
            return node

        return helper2()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
