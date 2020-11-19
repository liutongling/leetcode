#字符串 S 由小写字母组成。
#我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。
#返回一个表示每个字符串片段的长度的列表。
class Solution:
    def partitionLabels(self,S: str) -> list:
        long = len(S)
        #设置一个指针
        preindex = 0
        lastindex = 1
        #设置一个临时存放的字符串
        temp1 = ""
        temp2 = ""
        num = []
        #遍历字符串
        while lastindex <= long:
            temp1 = S[preindex:lastindex]
            temp2 = S[lastindex:]
            if len(set(temp1) & set(temp2)) == 0:
                num.append(len(temp1))
                preindex = lastindex
            lastindex+=1
        return num
if __name__ == '__main__':
    test = Solution()
    list_num=test.partitionLabels("ababcbacadefegdehijhklij")
    print(list_num)