#盛水最多的容器
class Solution:
    def maxArea(self,hight: list)->int:
        cont = len(hight)
        max_s = 0
        for index1 in range(cont):
            for index2 in range(index1+1,cont):
                if hight[index1] <= hight[index2]:
                    S = hight[index1]*(index2-index1)
                else:
                    S = hight[index2] * (index2 - index1)
                if max_s < S:
                    max_s =S
        return max_s

class Solution1:
    def maxArea(self,hight:list) ->int:
        #挑选两个最大的值
        #使用双指针方法
        S = 0
        pre_index = 0
        last_index =(len(hight)-1)
        while pre_index!=last_index:
            if hight[pre_index] < hight[last_index]:
                temp = hight[pre_index]*(last_index-pre_index)
                pre_index+=1
            else:
                temp = hight[last_index]*(last_index-pre_index)
                last_index-=1
            if temp > S:
                S = temp
        return S
#将一个list 表的索引和值生成一个字典然后将字典按照值排序
    def list_dict(self,sort_dict:list)->dict:
        sort = sorted(sort_dict)
        dict_sort = {}
        for i in range(len(sort)):
            dict_sort[i] = sort[i]
        return dict_sort
if __name__ == '__main__':
    test = Solution1()
    test_list = [1,8,6,2,5,4,8,3,7]
    #max_area = test.maxArea(test_list)
    sort_dict = test.maxArea(test_list)
    print(sort_dict)
    print(type(sort_dict))