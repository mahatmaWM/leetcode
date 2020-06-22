# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
#
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。 
#
# 示例 1: 
#
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
# 示例 2: 
#
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
#      给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
#      因此，当 n = 0 时，其格雷编码序列为 [0]。
# 
# Related Topics 回溯算法

# 思路，根据格雷码的递推性质：
# 设n阶格雷码集合为G(n)，则G(n+1)阶格雷码为：
# 1、给G(n)阶格雷码每个元素二进制形式前面添加 0，得到 G'(n)；
# 2、设G(n)集合倒序（镜像）为 R(n)，给 R(n)每个元素二进制形式前面添加 1，得到 R'(n)；
# 3、G(n+1) = G'(n) ∪ R'(n)，拼接两个集合即可得到下一阶格雷码。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
