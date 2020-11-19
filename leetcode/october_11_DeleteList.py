#here delete repeat element
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        index = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[index]:
                continue
            else:
                index+=1
                nums[index] = nums[i]
        return index+1
test = Solution()
liar = test.removeDuplicates([1,1,2])
print(liar)