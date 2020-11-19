#将两个排序的数组合并成一个数组
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_nums1 = 0
        index_nums2 = 0
        new_list = []
        index = 0
        while index_nums1 < m and index_nums2 < n:
            if nums1[index_nums1] < nums2[index_nums2]:
                new_list.append(nums1[index_nums1])
                index+=1
                index_nums1+=1
            else:
                new_list.append(nums2[index_nums2])
                index+=1
                index_nums2+=1
        while index_nums1 < m:
            new_list.append(nums1[index_nums1])
            index+=1
            index_nums1+=1
        while index_nums2 < n:
            new_list.append(nums2[index_nums2])
            index+=1
            index_nums2+=1
        return new_list
if __name__ == '__main__':
    test = Solution()
    test.merge()
