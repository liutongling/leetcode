#string go to number
class Solution:
    def myAtoi(self,string: str)->int:
        cont = len(string)
        num = 0
        for i in range(cont):
            if string[i]>='0' and string[i]<='9':
                num = int(string[i])+num*10
            elif num==0 and string[i]==' ' or string[i] == '+':
                continue
            elif num != 0 and (string[i]<'0' or string[i]>'9'):
                break
            elif num==0 and string[i] != ' ' and string[i] != '-':
                break
            elif num==0 and string[i] == '-':
                num = 0 - self.myAtoi(string[i+1:cont])
                if num < -2147483648:
                    return -2147483648
                else:
                    return num
        if num < -2147483648:
            return -2147483648
        elif num > 2147483648:
            return 2147483648
        else:
            return num
#find if -+ discover not return zero
class Solution1:
    def minus(self,s:str) ->int:
        cont = len(s)
        number = 0
        for i in range(cont):
            if s[i] >'0' and s[i]<'9':
                number = int(s[i]) +number*10
            else:
                break
        number = -number
        if number < -2147483648:
            return -2147483648
        elif number > 2147483648:
            return 2147483648
        else:
            return num
    def real(self,s:str) ->int:
        cont = len(s)
        number = 0
        for i in range(cont):
            if s[i] > '0' and s[i] < '9':
                number = int(s[i]) + number * 10
            else:
                break
        if number < -2147483648:
            return -2147483648
        elif number > 2147483648:
            return 2147483648
        else:
            return num
    def myAtoi(self,string: str) ->int:
        count = len(s)
        num = 0
        for i in range(count):
            if string[i]>='0' and string[i]<='9':#数字转换
                num = int(string[i])+num*10
            elif num==0 and string[i] != ' ' and string[i] != '-' and string[i] != '+':#非数字和符号 断
                break
            elif num==0 and string[i]==' ':#空格跳过
                continue
            elif num ==0 and string[i] == '+':
                num = self.real(string[i+1:count])
                return num
            elif num == 0 and string[i] == '-':
                num == self.minus(string[i+1:count])
                return num
        if num < -2147483648:
            return -2147483648
        elif num > 2147483648:
            return 2147483648
        else:
            return num
test = Solution()
number = test.myAtoi("+-12")
print(number)

