class Solution:
    def bubSort(self, numbers: list) -> list:
        for i in range(len(numbers)):
            for j in range(len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers
    def relativeSortArray(self, arr1: list, arr2: list) -> list:
        arr1Number = len(arr1)
        arr2Number = len(arr2)
        idx = []
        for i in arr2:
            if i in arr1:
                for j in range(len(arr1)):
                    if arr1[j] == i:
                        idx.append(j)
        print(idx)
        #arr1.sort()
        print(arr1)
        newarr1 = []
        for i in range(len(idx)):
            newarr1.append(arr1[idx[i]])
        #arr1.sort()
        for j in range(len(arr1)):
            if j not in idx:
                newarr1.append(arr1[j])

        newarr1[len(idx):]=self.bubSort(newarr1[len(idx):])
        return newarr1
if __name__ == '__main__':
    test = Solution()
    te = test.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])
    print(te)