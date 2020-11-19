#几种排序算法的实现
import sys
import numpy as np
sys.setrecursionlimit(900000000)  # 这里设置大一些
class Sorted():
    def bubSort(self,numbers:list)->list:
        for i in range(len(numbers)):
            for j in range(len(numbers)-i-1):
                if numbers[j] < numbers[j+1]:
                    temp = numbers[j]
                    numbers[j] = numbers[j+1]
                    numbers[j+1] = temp
        return numbers
    def selectSort(self,numbers:list)->list:
        index = 0
        for i in range(len(numbers)):
            min = numbers[i]
            for k in range(i,len(numbers)):
                #选择最小的一个数字
                if min > numbers[k]:
                    min = numbers[k]
                    index = k
                    judge = True
            if judge :
                numbers[i],numbers[index] = numbers[index],numbers[i]
                judge = False
        return numbers
    #归并两个列表
    def __mergered(self,a,b)->list:
        longA = len(a)
        longB = len(b)
        merger = []
        longAindex = 0
        longBindex = 0
        while longAindex<longA and longBindex<longB:
            if a[longAindex]<b[longBindex]:
                merger.append(a[longAindex])
                longAindex+=1
            else:
                merger.append(b[longBindex])
                longBindex+=1
        while longAindex<longA:
            merger.append(a[longAindex])
            longAindex+=1
        while longBindex<longB:
            merger.append(b[longBindex])
            longBindex+=1
        return merger

    def mergerSort(self,numbers:list)->list:
        #实现归并排序
        if len(numbers)==1:
            return numbers
        mid = len(numbers)//2
        a = self.mergerSort(numbers[:mid])
        b = self.mergerSort(numbers[mid:])
        return self.__mergered(a,b)
        #进行数据的分裂

    def quickSort(self,numbers:list,l:int,r:int)->list:
        i,j = l,r
        x = numbers[l]
        while i<j:
            while i<j and numbers[j]>=x:
                j-=1
            if i<j:
                numbers[i] = numbers[j]
                i+=1
            while i<j and numbers[i]<=x:
                i+=1
            if i<j:
                numbers[j] = numbers[i]
                j-=1
        numbers[i] = x
        self.quickSort(numbers[l:i],l,i-1)
        self.quickSort(numbers[i+1:],i+1,r)
    #快速排序
    #并没有搞明白怎么写的
    def quick_sort(self,array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            # print('right',array)
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
            # print('left',array)
        array[right] = key
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)


if __name__ == "__main__":
    for _ in range(1):
        arr = np.random.randint(0, 100, size=[10])
    print(arr)
    sorted_arr = np.sort(arr)
    test = Sorted()
    rear = np.size(arr)-1
    test.quick_sort(arr,0,rear)

    sorted_arr = np.sort(arr)
    print(arr)
    #assert (sorted_arr.all() == arr.all())
