# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
#
# 
#
# 
#
# 
#
# 示例： 
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
# 
#
# 
#
# 注意： 
#
# 
# 你可以重复使用键盘上同一字符。 
# 你可以假设输入的字符串将只包含字母。 
# Related Topics 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        T = []
        list1 = list(set('qwertyuiop'))
        list2 = list(set('asdfghjkl'))
        list3 = list(set('zxcvbnm'))

        def match(list0, str1):
            str1 = list(set(str1.lower()))
            for i in range(len(str1)):
                if str1[i] not in list0:
                    return False
            return True

        for i in range(len(words)):
            if match(list1, words[i]) is True or \
                    match(list2, words[i]) is True or \
                    match(list3, words[i]) is True:
                T.append(words[i])
        return T

# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().findWords(words=["Hello", "Alaska", "Dad", "Peace"]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
