#岛屿周长
#给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 表示水域。
#网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
#岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
class Solution:
    def islandPerimeter(self,grid:list)->int:
        length = len(grid)
        wide = len(grid[0])
        long = 0
        for i in range(length):
            for j in range(wide):
                if grid[i][j] == 1:
                    #判断四个方向
                    up  = i-1
                    down = i+1
                    lift = j-1
                    right = j+1
                    #上方
                    if up < 0:
                        long+=1
                    elif grid[up][j]==0:
                        long+=1
                    #下方
                    if down >=length:
                        long+=1
                    elif grid[down][j]==0:
                        long+=1
                    #左方
                    if lift < 0:
                        long+=1
                    elif grid[i][lift]==0:
                        long+=1
                    if right >= wide:
                        long+=1
                    elif grid[i][right]==0:
                        long+=1
        return long

    def multiply(self, num1: str, num2: str) -> str:
        number1 =  int(num1)
        number2 = int(num2)
        return str(number1*number2)
if __name__ == '__main__':
    test = Solution()
    long = test.islandPerimeter([[1,1]])
    print(long)