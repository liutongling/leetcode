#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        long_needle = len(needle)
        long_number = len(haystack)
        if needle == "":
            return 0
        if long_needle==1 and long_number==1 and haystack == needle:
            return 0
        index = -1
        for i in range(long_number-long_needle+1):
            temp = haystack[i:i+long_needle]
            if temp == needle:
                index = i
                break
        return index