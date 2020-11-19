#找出最接近目标数的 列表中三位数字
class Solution:
    #和三数之和类似
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums_sorted = sorted(nums)
        long = len(nums_sorted)
        #设置一个存储最小数字的变量
        if long == 3:
            return sum(nums_sorted)
        min = 100000000000000000000000000000000000000000000000000000000000
        sum1 = 0
        for i in range(long-2):
            #前后索引
            pre_index = i+1
            last_index = long-1
            while pre_index!=last_index:
                temp = (nums_sorted[i] +nums_sorted[pre_index]+nums_sorted[last_index])-target
                ab = abs(temp)
                if min >= ab:
                    min = ab
                    sum1 = (nums_sorted[i] +nums_sorted[pre_index]+nums_sorted[last_index])
                if temp >0:
                    last_index-=1
                else:
                    pre_index+=1
        return sum1
if __name__ == '__main__':
    test = Solution()
    li = [1,1,1,1]
    print(test.threeSumClosest(li,0))
