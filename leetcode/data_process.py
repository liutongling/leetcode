import linecache
import os
import sys
class Data:
    def getline(self,the_file_path,line_number):
        if line_number < 1:
            return ""
        for cur_line_number,line in enumerate(open(the_file_path,'r')):
            if cur_line_number == line_number-1:
                return line
    def get_str(self,filepath1,filepath2,line_number):
        line1 = self.getline(filepath1,line_number)
        line2 = self.getline(filepath2,line_number)
        line1_str1 = line1.split(" ")
        line1_str2 = line2.split(" ")
        list_str1_1 = line1_str1[1:4]
        list_str2_2 = line1_str2[1:4]
        li_temp = []
        for i in range(len(list_str1_1)):
            it = float(list_str1_1[i]) * 0.1 + float(list_str2_2[i]) * 0.2
            li_temp.append(round(it, 2))
        str1 = ""
        for i in range(len(li_temp)):
            number = li_temp[i]
            str1 = str1 + repr(number) + " "
        return str1
    def file_new(self,filepath,filepath1,filepath_new):
        with open(filepath) as file_class:
            readline = file_class.readlines()
            readline1 = readline[:-2]
            with open(filepath_new,"a+") as filewen:
                for file_line in readline1:
                    filewen.write(file_line)
        #filepath9 = self.getline(filepath.9)
        file_1 = self.get_str(filepath, filepath1, 9)
        file_2 = self.get_str(filepath, filepath1, 10)
        with open(filepath_new, 'a+') as filewen2:
            filewen2.write(file_1)
            filewen2.write("\n")
            filewen2.write(file_2)
if __name__ == '__main__':
    #生成类对象
    test = Data()
    test.file_new(sys.argv[1],sys.argv[2],sys.argv[3])