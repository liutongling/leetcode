class Solution:
    def validMountainArray(self, A: list) -> bool:
        index = 1
        count = 0
        while index<len(A)-1:
            pre = 0
            last = index + 1
            while pre<index:
                if A[pre]<A[index]:
                    pre+=1
                else:
                    break
            while last<len(A):
                if A[last]<A[index]:
                    last+=1
                else:
                    break
            if index == pre and len(A) == last :
                #return True
                #break
                count+=1

            index += 1
        if count == 1:
            return True
        elif index == len(A)-1 or count!=1:
            return False
    def test(self,A:list)->bool:
        if len(A)<3:
            return False
        index = 0
        while index<len(A)-1:
            if A[index]<A[index+1]:
                index+=1
            else:
                last = index
                while last<len(A)-1:
                    if A[last]>A[last+1]:
                        last+=1
                    else:
                        break
                if last==len(A)-1 and index !=0:
                    return True
                else:
                    return False
    #失败并没有实现
    '''
    def nextPermutation(self, nums: list) -> None:
        longNumber = len(nums)
        #while index<longNumber:
        #    if nums[pre]>nums[index]:
        #        index+=1
        #if index==longNumber:
        #    return nums.sort()
        #重新开始
        pre = 0

        #存取差值
        dis = 0
        #存取最小的那个差值
        #
        while pre < longNumber-1:
            index = pre + 1
            #记录一个其中一个查找，方便寻找最小差值
            minDis = -(nums[pre]-nums[index])
            record = index
            count = 0
            while index<longNumber:
                dis = nums[pre] - nums[index]
                if dis >= 0:
                    index+=1
                    continue
                else:
                    count = 1
                    if minDis < dis:
                        minDis = dis
                        record = index
    '''


    # def nextPermutation(self,nums:list)->list:
    #     #指定尾
    #     last = len(nums)-1
    #     while last>0:
    #         pre = last-1
    #         while pre >= 0:
    #             if nums[pre] > nums[last]:
    #                 #self.nextPermutation(nums[:-1])
    #                 pre-=1
    #             else:
    #                 nums[pre],nums[last] = nums[last],nums[pre]
    #                 self.nextPermutation(nums[pre+1:])
    #                 return nums
    #         if pre == 0:
    #             last -= 1
    #     if last == 0:
    #         return nums.reverse()
    def bubSort(self,numbers:list)->list:
        for i in range(len(numbers)):
            for j in range(len(numbers)-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j],numbers[j+1]  = numbers[j+1],numbers[j]
        return numbers
    def nextPermutation(self, nums: list) -> None:
        #指定尾
        last = len(nums)-1
        while last>0:
            pre = last-1
            while pre >= 0:
                if nums[pre] >= nums[last]:
                    #self.nextPermutation(nums[:-1])
                    pre-=1
                else:
                    nums[pre],nums[last] = nums[last],nums[pre]
                    nums[pre+1:] = self.bubSort(nums[pre+1:])

                    return None
            if pre == -1:
                last -= 1
        if last == 0:
            nums.reverse()
            return None



if __name__ == '__main__':
    test = Solution()
    #numTest = [1,1,5]
    #numTest = [1, 2, 3]
    numTest1= [1,2,3,6,5]
    test.nextPermutation(numTest1)
    print(numTest1)