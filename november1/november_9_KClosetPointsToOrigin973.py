class Solution:
    def kClosest(self, points: list, K: int) -> list:
        #PointsNumber = len(points)
        for j in range(k):
            minNumber = 10000
            for i in points:
                if i not in res:
                    temp = i[0]**2+i[1]**2
                    if temp < minNumber:
                        minNumber = temp
                        templist = i
            res.append(templist)
        return res

    def convertToTitle(self, n: int) -> str:
        # dictAlphabet = {0:'A',1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}
        dictAlphabet = {0:"A",1: 'A', 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K",
                        12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U",
                        22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
        c=''
        str= ''
        if n <= 26:
            return dictAlphabet[n % 27]
        else:
            while n>26:
                k = n//26
                str = str +"A"
                n = k

            str =str+  dictAlphabet[n%27]
            n = n//26
            return str
if __name__ == '__main__':
    test = Solution()
    print(test.convertToTitle(27))
