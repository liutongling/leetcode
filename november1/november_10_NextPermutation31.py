class Solution:
    def bubSort(self,numbers:list)->list:
        for i in range(len(numbers)):
            for j in range(len(numbers)-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j],numbers[j+1]  = numbers[j+1],numbers[j]
        return numbers
    def nextPermutation(self, nums: list) -> None:
        #指定尾
        pre = 0
        while pre < len(nums)-2:
            if nums[pre]>nums[pre+1]:
                pre+=1
            else:
                break
        if pre==len(nums)-2:
            return nums.reverse()

        last = len(nums)-1
        #找到第一个升序对
        while last >= 1:
            if nums[last]<nums[last-1]:
                last-=1
            else:
                last-=1
                break
        if last==0:
            return nums.reverse()
        else:
            lastnext = len(nums)-1
            while lastnext > last:
                if nums[lastnext]>nums[last]:
                    nums[lastnext],nums[last]=nums[last],nums[lastnext]
                    #将后面的进行降序排列
                    nums[last + 1:] = self.bubSort(nums[last+ 1:])
                    break
                else:
                    lastnext-=1
            if lastnext == 0:
                return nums.reverse()
            else:
                return nums

if __name__ == '__main__':
    test = Solution()
    print(test.nextPermutation([5,1,1]))
