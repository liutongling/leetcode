class Solution:
    #将字符串转换为整数
    def toNumber(self,s:str)->int:
        return int(s[2:])
    #统计一的个数
    def countOne(self,num:int)->int:
        count = 0
        while num>0:
            if num %10 == 1:
                count+=1
            num = num//10
        return count

    def sortByBits(self, arr: list) -> list:
        #设置一个字典将数组里面的值作为键
        dictNumber = dict()
        for i in arr:
            dictNumber[i] = self.countOne(self.toNumber(bin(i)))
        #print(dictNumber)
        jieshu = dict(sorted(dictNumber.items(),key=lambda x:(x[1],x[0])))#d.items(), key=lambda kv: (-kv[1], kv[0])
        print(jieshu)
        res = []
        for i in jieshu:
            for _ in range(arr.count(i)):
                res.append(i)
        return res
if __name__ == '__main__':
    test = Solution()
    print(test.countOne(test.toNumber(bin(8))))
    te= test.sortByBits([1024,512,256,128,64,32,16,8,4,2,1])

    print(te)