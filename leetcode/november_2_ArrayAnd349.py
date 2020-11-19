#
class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        setNumber = set(nums1)
        setnumber1 = set(nums2)
        return list(setNumber&setnumber1)