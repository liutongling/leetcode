#矩阵化
import numpy as np
import re
import sys
pathfile="D:\data\O1.txt"
pathfile1="D:\data\O11.txt"
class DataMarix:
    def angle(self,y):
        c = np.linalg.eig(y)
        d = c[1]
        e = np.dot(np.dot(np.linalg.inv(d), y), d)
        e = np.around(e, decimals=4, out=None)
        return list(e)
    def input_file(self,path,line):
        with open(path,'a+') as file:
            file.write(line)
    #接受矩阵，将矩阵转换问文本文件进行存储
    def matrix_file(self,path,test_1):
        with open(path,'a+') as file:
            str_temp = ''
            for i in range(len(test_1)):
                for k in range(len(test_1[i])):
                    str_temp = str_temp + str(test_1[i][k]) + ' '
                file.write(str_temp)
                file.write('\n')
                str_temp = ''
    def test2(self,path,path1):
        with open(path,'r') as file:
            file_lines = file.readlines()
            cont = 0
            temp = []
            for line in file_lines:
                #使用正则表达式匹配字符串中的浮点数
                m = m=re.findall(u"(-?)(([1-9]\\d*\\.\\d*)|(0\\.\\d*[1-9]\\d*)|([1-9]\\d*))",line)
                temp1 = []
                if len(m) == 3:
                    for i in range(len(m)):
                        if '-' in m[i]:
                            num = 0-float(m[i][1])
                        else:
                            num=float(m[i][1])
                        temp1.append(num)
                    cont+=1
                    temp.append(temp1)
                else:
                    #将不符合的行进行写入文件
                    self.input_file(path1,line)
                if cont%3==0 and cont!=0 and len(temp)!=0:
                    dui_list = self.angle(temp)
                    self.matrix_file(path1,dui_list)
                    print("**%d",(cont))
                    temp = []
if __name__ == '__main__':
    s = DataMarix()
    s.test2(pathfile,pathfile1)