# 给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。
# 如果不存在这样的32位整数，则返回-1。
#
# 示例 1: 
#
# 
# 输入: 12
# 输出: 21
# 
#
# 示例 2: 
#
# 
# 输入: 21
# 输出: -1
# 
# Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n, tail = list(str(n)), []
        for i in range(len(n)-1, -1, -1):
            # tail保存了倒序遍历n的每位数字的信息，逆序找到一位j比i更大，交换i j的数字，然后把后面的升序排，最后组合成新的数字
            # 方法与31题一样
            for j in tail:
                if n[j] > n[i]:
                    n[j], n[i] = n[i], n[j]
                    m = int(''.join(n[:i + 1] + sorted(n[i + 1:])))
                    return -1 if m > 2 ** 31 - 1 else m
            tail.append(i)
        return -1


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().nextGreaterElement(n=21))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
