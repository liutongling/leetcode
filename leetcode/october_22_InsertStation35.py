#给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
class Solution:
    def searchInsert(self,nums: list,target: int) ->int:
        if target in nums:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
        else:
            for k in range(len(nums)):
                if target > nums[k]:
                    continue
                else:
                    nums.insert(target,k)
                    return k
            if target >nums[-1]:
                nums.append(target)
                return len(nums)-1

if __name__ == '__main__':
    test = Solution()
    print(test.searchInsert([1,3,5,6], 7))