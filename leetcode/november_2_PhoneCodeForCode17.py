class Solution:

    def letterCombinations(self, digits: str) ->list:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        def back(connect,digitsubset):

            if len(digitsubset)==0:
                res.append(connect)
            else:
                for letter in phone[digitsubset[0]]:
                    back(connect+letter,digitsubset[1:])
        back('',digits)
        return res
if __name__ == '__main__':
    test = Solution()
    listtest=test.letterCombinations("23")
    print(listtest)