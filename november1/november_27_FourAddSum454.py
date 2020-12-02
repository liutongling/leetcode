#题目描述
#给定四个包含相同数目得整数数组，从这个四个数组中各找一个数组使之相加为零。其中i,j,k,l为四个的索引
#有多少种满足上述条件的索引。
from collections import Counter
class Solution:
    #暴力解法
    # def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
    #     sum = []
    #     for i in range(len(A)):
    #         for j in range(len(B)):
    #             for k in range(len(C)):
    #                 for l in range(len(D)):
    #                     temp = []
    #                     if A[i]+B[j]+C[k]+D[l]==0:
    #                         temp.append(i)
    #                         temp.append(j)
    #                         temp.append(k)
    #                         temp.append(l)
    #                         if len(temp)!=0:
    #                             print(temp)
    #                             sum.append(temp)
    #     return len(sum)
    #使用哈希表和分组进行解决
    def fourSumCount(self, A: list, B: list, C: list, D: list) -> int:
        #使用字典
        ans = 0
        li =  Counter(u+v for u in A for v in B)
        for i in C:
            for j in D:
                if (-j-i) in li:
                    ans += li[-j-i]
        return ans
if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1]))