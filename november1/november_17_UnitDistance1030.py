class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> list:
        distance = []
        for i in range(R):
            for j in range(C):
                distance.append([i,j])
        print(distance)
        newdistance = sorted(distance,key=lambda x :(abs(r0-x[0])+abs(c0-x[1])))
        return newdistance

    def alphabetBoardPath(self, target: str) -> str:
        pass

    def longestValidParentheses(self, s: str) -> int:
        inn = []
        dictk = {")":"("}
        for i in s:
            if (i == ")" or i == "(" )and len(inn)==0:
                inn.append(i)
            elif i=="(":
                inn.append(i)
            else:
                if dictk[i] == inn[-1]:
                    inn.pop()
                else:
                    inn.append(i)
        print(dictk[i] == inn[-1])
        return len(s) - len(inn)
    #实现对排序,使用数组实现堆
    def parent(self,i:int):
        return int(((i+1)/2) )- 1
    def left(self,i:int):
        return 2*(i+1)-1
    def right(self,i:int):
        return 2*(i+1)
    #将数组建立成堆
    def contrationHeapSort(self,Numbers:list)->list:
        long = len(Numbers)
        for i in range(long):
            if self.parent(i)<0:
                continue
            else:
                temp = self.parent(i)
                k = i
                while temp >=0:
                    if Numbers[temp] < Numbers[k]:
                        Numbers[temp],Numbers[k] = Numbers[k],Numbers[temp]
                    k = temp
                    temp = self.parent(temp)
        return Numbers
    def maxify_heap(self,heap:list,size:int):
        parent = 0
        while self.left(parent) < size or self.right(parent) < size:
            max_val = heap[parent]
            child = parent
            if self.left(parent)< size and heap[self.left(parent)] > max_val:
                max_val = heap[self.left(parent)]
                child = self.left(parent)
            if self.right(parent)<size and heap[self.right(parent)]> max_val:
                max_val = heap[self.right(parent)]
                child = self.right(parent)
            if child == parent:
                return
            heap[parent],heap[child] = heap[child],heap[parent]
            parent = child
    def heapSort(self,A:list):
        A = self.contrationHeapSort(A)
        size = len(A)
        while size > 1:
            A[size-1],A[0] = A[0],A[size-1]
            size-=1
            self.maxify_heap(A,size)
        return A
if __name__ == '__main__':
    test = Solution()
    A = [1,3,4,2,9,7,8,10,15,17]
    print(test.heapSort(A))
    # dictk = {")": "("}
    # print(dictk[")"])
