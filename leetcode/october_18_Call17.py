#电话号码的字母组合
class Solution:
    dict_call={'2':{a,b,c},'3':{d,e,f},'4':{g,h,i},'5':{j,k,l},'6':{m,n,o},'7':{p,q,r,s},'8':{t,u,v},'9':{w,x,y,z}}
    def letterCombinations(self, digits: str) -> list:
        str_nums = len(digits)
        temp = []
        for i in range(str_nums):
            if digits[i] in self.dict_call.keys():
                temp.append(self.dict_call[digits[i]])
        cont = 1
        for k in range(len(temp)):
            cont=(temp[k])*cont
        for j in range(cont):
            if len(temp) != 0:
                for z in range(len())