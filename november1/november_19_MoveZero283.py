class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre = len(nums)-1
        count  = 0
        for i in nums:
            if i ==0:
                count+=1

        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            else:
                nums[i],nums[pre] = nums[pre],nums[i]
                pre-=1
                if  pre == len(nums)-count-1:
                    break
    def moveZeroes1(self,nums:list)->None:
        if len(nums)==1 or len(nums)==0:
            return
        prenums = 0
        count = 0
        for i in range(len(nums)):
            count = 0
            prezeros = []
            for j in range(len(nums)):
                if nums[j] == 0:
                    prezeros.append(j)
            if nums[i]!=0 and len(prezeros)!=0 and i>prezeros[count]:
                prenums = i
                nums[prezeros[count]],nums[prenums] = nums[prenums],nums[prezeros[count]]

if __name__ == '__main__':
    nums  = [4,2,4,0,0,3,0,5,1,0]
    s = Solution()
    s.moveZeroes1(nums)
    print(nums)