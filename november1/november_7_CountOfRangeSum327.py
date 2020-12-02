import bisect
class Solution:
    def countRangeSum(self, nums: list, lower: int, upper: int) -> int:
        longNumber = len(nums)
        count = 0
        for i in range(longNumber):
            sum = 0
            for j in range(i,longNumber):
                sum = sum + nums[j]
                if sum >= lower and sum <= upper:
                    count += 1
        return count

    def countRangeSum1(self, nums: list, lower: int, upper: int) -> int:
        res, pre, now = 0, [0], 0
        for n in nums:
            now += n
            res += bisect.bisect_right(pre, now - lower) - bisect.bisect_left(pre, now - upper)
            bisect.insort(pre, now)
        return res
if __name__ == '__main__':
    test = Solution()
    count = test.countRangeSum1([-2,5,-1],-2,2)
    print(count)