class Solution:
    #寻找最小的值并且删除和返回
    # def minvalue(self,stringlist:str,s:str)->str:
    #     minvalue = stringlist[0]
    #     index = 0
    #     judge = 0
    #     for i in range(len(stringlist)):
    #         if stringlist[i]<minvalue and stringlist[i]>s:
    #             minvalue = stringlist[i]
    #             index = i
    #             judge = 1
    #
    #     return stringlist.pop(index)
    #
    # def maxvalue(self,stringlist:str,s:str)->str:
    #     maxvalue = stringlist[0]
    #     index = 0
    #     judge = 0
    #     for i in range(len(stringlist)):
    #         if stringlist[i]>maxvalue and stringlist[i]<s:
    #             maxvalue = stringlist[i]
    #             index = i
    #             judge =1
    #
    #     return stringlist.pop(index)
    #
    # def sortString1(self, s: str) -> str:
    #     liststring = list(s)
    #     new = ""
    #     while len(liststring)!=0:
    #         #寻找最小的字符
    #         new1 = ""
    #         if len(new1)==0:
    #             indexmin= liststring.index(min(liststring))
    #             new1 = new1+liststring.pop(indexmin)
    #             while len(self.minvalue(liststring,new1[-1]))!=0:
    #                 new1=new1+self.minvalue(liststring,new1[-1])
    #         new2=""
    #         if len(new2)==0:
    #             indexmax = liststring.index(max(liststring))
    #             new2 = new2+liststring.pop(indexmax)
    #             while len(self.maxvalue(liststring,new2[-1]))!=0:
    #                 new2=new2+self.maxvalue(liststring,new2[-1])
    #         new = new1+new2
    #     return new
    def allmin(self,s:list,c:str)->list:
        l = []
        for i in s:
            if i>c:
                l.append(i)
        return l
    def secondmin(self,string:list,c:str)->str:
        l = self.allmin(string,c)
        if len(l)==0:
            return ""
        return min(l)
    def allmax(self,s:list,c:str)->list:
        l = []
        for i in s:
            if i<c:
                l.append(i)
        return l
    def secondmax(self,string:list,c:str)->str:
        l = self.allmax(string,c)
        if len(l)==0:
            return ""
        return max(l)
    def sortString(self, s: str) -> str:
        liststring = list(s)
        newstring = ""
        while len(liststring)!=0:
            new = ""
            #抽取最小的值
            m = min(liststring)
            new = new+ m
            liststring.pop(liststring.index(m))
            #删除
            while len(self.secondmin(liststring,new[-1]))==1:
                temp = self.secondmin(liststring,new[-1])
                new = new + self.secondmin(liststring,new[-1])
                if temp =="":
                    break
                numberindex = liststring.index(temp)
                liststring.pop(numberindex)
            new1 = ""
            #抽取最大值
            if len(liststring)!=0:
                m = max(liststring)
                new1 = new1 + m
                liststring.pop(liststring.index(m))
                while len(self.secondmax(liststring,new1[-1]))==1:
                    temp = self.secondmax(liststring,new1[-1])
                    new1 = new1 + self.secondmax(liststring,new1[-1])
                    if temp =="":
                        break
                    numberindex = liststring.index(temp)
                    liststring.pop(numberindex)
            newstring = newstring +new +new1
        return newstring

    def spiralOrder(self, matrix: list) -> list:
        #记录横纵的大小
        n = len(list)
        m = len(list[0])
        for i in range(9):
            pass
if __name__ == '__main__':
    t = Solution()
    new = t.sortString("rat")
    print(new)