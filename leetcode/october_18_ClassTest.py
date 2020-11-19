class Mao:
    def __init__(self):
        print("I am cat")
    def eat(self,string:str):
        print("I can eat %s"%(string))
class Other:
    def test(self,other:Mao,string):
        other.eat(string)
class Other1(Mao):
    #def __init__(self):
    #    print("I am Other1")
    def testMao(self,string:str):
        self.eat(string)
if __name__ == '__main__':
    #te = Mao()
    test = Other1()
    test.testMao("maoliang")