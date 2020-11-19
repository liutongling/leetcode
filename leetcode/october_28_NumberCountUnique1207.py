#给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
#如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
class Solution:
    def uniqueOccurrences(self,arr:list)->bool:
        #定义一个数组，用来存放统计数目
        number_set = set(arr)
        nuber_count = []
        for i in number_set:
            count = 0
            for k in arr:
                if i == k:
                    count+=1
            if count in nuber_count:
                return False
            else:
                nuber_count.append(count)
        if len(number_set) == len(nuber_count):
            return True