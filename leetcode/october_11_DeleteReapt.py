class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if val == nums[i]:
                continue
            else:
                nums[index] = nums[i]
                index += 1
        return index
test = Solution()
print(test.removeElement([3,2,2,3],3))
