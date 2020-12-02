class Solution:
    def reversePairs(self, nums: list) -> int:
        long = len(nums)
        count = 0
        for i in range(long):
            for j in range(i+1,long):
                if nums[i]>2*nums[j]:
                    count+=1
        return count
    #使用二维列表
    def reversePairs1(self, nums: list) -> int:
        #进行第一遍遍历创建索引
        temp = []
        for i in range(len(nums)):
            temp1 = []
            temp1.append(i)
            temp1.append(nums[i])
            temp.append(temp1)
        #将二维列表进行排序
        n = sorted(temp,key = lambda x:x[1],reverse=True)
        #print(n)
        count = 0
        #使用n 二维数组进行统计
        for i in range(len(n)):
            #判断到达的位置
            judge = []
            for j in range(i,len(n)):
                if n[i][1]> 2*n[j][1]:
                    #print(j)
                    judge.append(j)
                    break
            #print(judge)
            for x in judge:
                for k in range(x,len(n)):
                    if n[i][0]< n[k][0]:
                        #print(n[i][0],n[k][0])
                        count+=1
        return count
    #使用归并排序
    def reversePairs2(self, nums: list) -> int:
        long = len(nums)
        if long==0 or long==1:
            return 0
        num1=nums[0:long//2]
        num2=nums[long//2:]
        count = 0
        num1Sort = sorted(num1)
        num2Sort = sorted(num2)
        for i in range(len(num1Sort)):
            for j in range(len(num2Sort)):
                if num1Sort[i]>2*num2Sort[j]:
                    count+=1
                else:
                    break
        count1 = self.reversePairs2(num1)
        count2 = self.reversePairs2(num2)
        return count+count1+count2

    #归并排序
    def SortedMerage(self,nums):
        if len(nums)==1:
            return nums
        mid = len(nums)//2
        new1 = self.SortedMerage(nums[:mid])
        new2 = self.SortedMerage(nums[mid:])
        long1 = len(new1)
        long2 = len(new2)
        i , j = 0 , 0
        new = []
        while i<long1 and j <long2:
            if new1[i]< new2[j]:
                new.append(new1[i])
                i+=1
            else:
                new.append(new2[j])
                j+=1
        while i<long1:
            new.append(new1[i])
            i+=1
        while j<long2:
            new.append(new2[j])
            j+=1
        return new
if __name__ == '__main__':
    s = Solution()
    n = s.SortedMerage([2,4,3,5,1])
    print(n)