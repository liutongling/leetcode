#有多少小于当前数字的数字
class Solution:
    def smallerNumbersThanCurrent(self,nums:list)->list:
        temp = []
        for i in nums:
            count = 0
            for j in nums:
                if  j<i:
                    count+=1
            temp.append(count)
        return temp
if __name__ == '__main__':
    test = Solution()
    test_list = test.smallerNumbersThanCurrent([8,1,2,2,3])
    print(test_list)