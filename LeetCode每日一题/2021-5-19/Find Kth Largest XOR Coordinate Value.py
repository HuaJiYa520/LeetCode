# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Find Kth Largest XOR Coordinate Value
   Description :
   Author :        HuaJi
   date：          2021/5/19
-------------------------------------------------

"""


# 常规思路：遍历整个矩阵，然后依次计算每个位置的值，存储到result_list中，最后将list排序，输出需要的结果。
# 效率非常低下,提交结果不出意外的超时

class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        result_list = []
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):

                temp_sum = 0
                for i in range(0, x + 1):
                    for j in range(0, y + 1):
                        temp_sum ^= matrix[i][j]
                result_list.append(temp_sum)

        result_list.sort(reverse=True)
        return int(result_list[k - 1])


# 官方解法：使用二维前缀和

class Solution2:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        results = list()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] ^ pre[i][j - 1] ^ pre[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                results.append(pre[i][j])

        results.sort(reverse=True)
        return results[k - 1]


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/solution/zhao-chu-di-k-da-de-yi-huo-zuo-biao-zhi-mgick/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    matrix = [[5, 2], [1, 6]]
    k = 2
    s = Solution2()
    v = s.kthLargestValue(matrix, k)
    print(v)
