#Given an array A of positive lengths, return the largest perimeter
# of a triangle with non-zero area, formed from 3 of these lengths.

#If it is impossible to form any triangle of non-zero area, return 0.
class Solution:
    def judge(self,a,b,c):
        if a+b > c:
            return True
    def largestPerimeter(self, A: list) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if self.judge(A[i+2],A[i+1],A[i]):
                return A[i]+A[i+1]+A[i+2]
        return 0

if __name__ == '__main__':
    s =Solution()
    ss=s.largestPerimeter([3,6,2,3])
    print(ss)