import random
class Fish:
    def __init__(self):
        self.x=random.randrange(0,11)
        self.y=random.randrange(0,11)
    def move(self):
        direction = random.randrange(0,4)
        if direction == 0:
            self.x= self.x+1
            if self.x > 10:
                self.x =  10 - (self.x-10)
        elif direction == 1:
            self.x=self.x-1
            if self.x < 0:
                self.x = self.x + 2
        elif direction == 2:
            if self.y > 10:
                self.y = 10 - (self.y-10)
        elif direction == 3:
            if self.y < 0:
                self.y = self.y + 2
class Turle:
    def __init__(self):
        self.x = random.randrange(0, 11)
        self.y = random.randrange(0, 11)
        self.energy = 100
    def move(self):
        direction = random.randrange(0,4)
        if direction == 0:
            self.x= self.x+random.randrange(1,3)
            if self.x == 11:
                self.x = 9
            if self.x ==12:
                self.x = 8
        elif direction == 1:
            self.x= self.x-random.randrange(1,3)
            if self.x == -1:
                self.x = 1
            if self.x == -2:
                self.x = 2
        elif direction == 2:
            self.y= self.y+random.randrange(1,3)
            if self.y == 11:
                self.y = 9
            if self.y ==12:
                self.y = 8
        elif direction == 3:
            self.y= self.y-random.randrange(1,3)
            if self.y == -1:
                self.y =1
            if self.y==-2:
                self.y = 2
        self.energy-=1
    def eat(self,fish:Fish)->int:
        x = 0
        if self.y==fish.y and self.x==fish.x:
            self.energy = self.energy+20
            x = 1
        if self.energy > 100:
            self.energy = 100
        print("吃了一个鱼儿 能量剩余 %d（此时坐标：%d %d）" % (self.energy,self.x,self.y))
        return x
if __name__ == '__main__':
    #创建十个鱼儿和一个乌龟放在list里面
    list_fish=[]
    turle=Turle()
    cont = 0
    for k in range(0,10):
        list_fish.append(Fish())
    while len(list_fish)!=0 and turle.energy!=0:
        print("第%d次移动"%cont)
        for i in list_fish:
            judge = turle.eat(i)
            print("还剩下 %d 条鱼儿" %len(list_fish))
            if judge == 1:
                list_fish.remove(i)
        # 鱼儿和乌龟开始移动
        turle.move()
        for i in list_fish:
            i.move()
        cont+=1
        if turle.energy == 0:
            print("乌龟输了")
        if len(list_fish) == 0:
            print("鱼儿输了")


