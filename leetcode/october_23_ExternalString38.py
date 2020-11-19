class Solution:
    def countAndSay(self,n:int)->str:
        if n < 0 or n > 30:
            return ""
        temp = "1"
        if n == 1:
            return temp
        else:
            for i in range(1,n+1):
                for i in temp:
                    

