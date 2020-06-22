# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。
# 这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 示例: 
#
# 你可以将以下二叉树：
#
#    1
#   / \
#  2   3
#     / \
#    4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
#
# 提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
# 你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。 
# Related Topics 树 设计

# 树的遍历和恢复问题，常见的遍历方法不会输出叶子后面的none标识，所以至少需要中序+（前序 或者 后序）才能恢复。
# none对确定叶子节点是有帮助的，有它选择 前序或者后序 一种遍历方式即可恢复树结构。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = []

        def helper1(root):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
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
        
        :type data: str
        :rtype: TreeNode
        """
        d = iter(data.split(","))

        def helper2():
            tmp = next(d)
            # print(tmp)
            if tmp == "#":
                return
            node = TreeNode(int(tmp))
            node.left = helper2()
            node.right = helper2()
            return node

        return helper2()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    print(codec.serialize(root))
    codec.deserialize(codec.serialize(root))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
