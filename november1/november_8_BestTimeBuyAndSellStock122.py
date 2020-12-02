class Solution:
    def maxProfit(self, prices: list) -> int:
        longNumber = len(prices)
        sum = 0
        for i in range(longNumber-1):
            if prices[i]<prices[i+1]:
                sum = sum + prices[i+1]- prices[i]
        return sum
    #最大子序和
    def maxSubArray(self, nums: list) -> int:
        longNumber = len(nums)
        maxnumber = min(nums)
        for i in range(longNumber):
            sum = 0
            for j in range(i,longNumber):
                sum = sum + nums[j]
                if maxnumber<= sum:
                    maxnumber = sum
        return maxnumber

    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        gradeLevel = len(list)//2
        if len(list)%2==1:
            gradeLevelIn = gradeLevel+1
        else:
            gradeLevelIn = gradeLevel
        for i in range(gradeLevel):
            for j in range(gradeLevelIn):
                temp=matrix[i][len(matrix)-1-j]
                matrix[i][len(matrix)-1-j]=matrix[i][j]
if __name__ == '__main__':
    test = Solution()
    money = test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(money)