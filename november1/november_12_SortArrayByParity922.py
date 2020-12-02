class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        oddNumber = []
        evenNumber = []
        for i in A:
            if i%2==0:
                evenNumber.append(i)
            else:
                oddNumber.append(i)
        evenNumber.sort()
        oddNumber.sort()
        even = 0
        odd = 0
        for i in range(len(A)):
            if i%2==0:
                A[i] = evenNumber[even]
                even+=1
            else:
                A[i] = oddNumber[odd]
                odd+=1
        return A