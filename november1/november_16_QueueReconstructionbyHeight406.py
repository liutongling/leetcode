class Solution:

    def reconstructQueue(self, people: list) -> list:
        people.sort(key=lambda x:(x[0]+x[1],x[0]))
        return people

    def singleNumber(self, nums: list) -> int:
        temp = []
        temp.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] in temp:
                temp.remove(nums[i])
            else:
                temp.append(nums[i])
        return temp[0]
if __name__ == '__main__':
    test = Solution()
    print(test.singleNumber([1,1,2,3,3,4,4]))