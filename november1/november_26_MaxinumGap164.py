class Solution:
    def maximumGap(self, nums: list) -> int:
        nums.sort()
        li = []
        for i in range(1,len(nums)):
            li.append(nums[i]-nums[i-1])
        return max(li)
    def climbStairs(self, n: int) -> int:
        q = 1
        p = 0
        count = 0
        for i in range(1,n+1):
            temp = q
            q = q+p
            p = temp

        return q
if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))
