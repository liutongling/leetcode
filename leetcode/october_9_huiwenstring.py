#define soltion class
class Solution:
    def judge(self,s: str)->bool:
        head = 0
        tail = len(s) - 1
        num = len(s) // 2
        k = 0
        for i in range(num):
            if s[head] == s[tail]:
                head+=1
                tail-=1
                k+=1
            else:
                break
        if k == num:
            return True
        else:
            return False
    def longestPalindrome(self, s: str) -> str:
        number =  len(s)
        if number == 1:
            return s
        elif number == 2 and s[0] != s[1]:
            return s[0]
        li_str = []
        for i in range(number):
            for j in range(i+1,number):
                if self.judge(s[i:j+1]):
                    li_str.append(s[i:j+1])
        if len(li_str) == 0:
            return s[0]
        else:
            return max(li_str, key=len, default='')
test = Solution()
str_test = test.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")
print(str_test)