#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (48.69%)
# Likes:    258
# Dislikes: 0
# Total Accepted:    35.9K
# Total Submissions: 73.6K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
#
#
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
#
#
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"
#
#
#
# 参见网友喜刷刷的博客，首先我们要知道当n = 3时，其排列组合共有3! = 6种，当n = 4时，其排列组合共有4! = 24种，我们就以n = 4, k = 17的情况来分析，所有排列组合情况如下：
#
# 1234
# 1243
# 1324
# 1342
# 1423
# 1432
# 2134
# 2143
# 2314
# 2341
# 2413
# 2431
# 3124
# 3142
# 3214
# 3241
# 3412 <--- k = 17
# 3421
# 4123
# 4132
# 4213
# 4231
# 4312
# 4321
#
# 我们可以发现，每一位上1,2,3,4分别都出现了6次，当最高位上的数字确定了，第二高位每个数字都出现了2次，当第二高位也确定了，第三高位上的数字都只出现了1次，当第三高位确定了，那么第四高位上的数字也只能出现一次，下面我们来看k = 17这种情况的每位数字如何确定，由于k = 17是转化为数组下标为16：
#
# 最高位可取1,2,3,4中的一个，每个数字出现3！= 6次（因为当最高位确定了，后面三位可以任意排列，所以是3！，那么最高位的数字就会重复3！次），所以k = 16的第一位数字的下标为16 / 6 = 2，在 "1234" 中即3被取出。这里我们的k是要求的坐标为k的全排列序列，我们定义 k' 为当最高位确定后，要求的全排序列在新范围中的位置，同理，k'' 为当第二高为确定后，所要求的全排列序列在新范围中的位置，以此类推，下面来具体看看：
#
# 第二位此时从1,2,4中取一个，k = 16，则此时的 k' = 16 % (3!) = 4，注意思考这里为何要取余，如果对这24个数以6个一组来分，那么k=16这个位置就是在第三组（k/6 = 2）中的第五个（k%6 = 4）数字。如下所示，而剩下的每个数字出现2！= 2次，所以第二数字的下标为4 / 2 = 2，在 "124" 中即4被取出。
#
# 3124
# 3142
# 3214
# 3241
# 3412 <--- k' = 4
# 3421
#
# 第三位此时从1,2中去一个，k' = 4，则此时的k'' = 4 % (2!) = 0，如下所示，而剩下的每个数字出现1！= 1次，所以第三个数字的下标为 0 / 1 = 0，在 "12" 中即1被取出。
#
# 3412 <--- k'' = 0
# 3421
#
# 第四位是从2中取一个，k'' = 0，则此时的k''' = 0 % (1!) = 0，如下所示，而剩下的每个数字出现0！= 1次，所以第四个数字的下标为0 / 1= 0，在 "2" 中即2被取出。
#
# 3412 <--- k''' = 0
#
# 那么我们就可以找出规律了
# a1 = k / (n - 1)!
# k1 = k
#
# a2 = k1 / (n - 2)!
# k2 = k1 % (n - 2)!
# ...
#
# an-1 = kn-2 / 1!
# kn-1 = kn-2 % 1!
#
# an = kn-1 / 0!
# kn = kn-1 % 0!
# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, jiechengs = '', [1]
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        k -= 1
        for i in range(2, n + 1):
            jiechengs.append(jiechengs[-1] * i)

        for i in range(n):
            jc = jiechengs[n - i - 2]
            point = int(k / jc)
            k %= jc
            res += nums[point]
            nums.pop(point)
        return res
# @lc code=end

