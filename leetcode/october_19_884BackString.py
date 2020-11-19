#给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #遍历S和T 去掉退格字符
        s_list = []
        t_list = []
        for i in S:
            if i=='#':
                if len(s_list)!=0:
                    s_list.pop()
            else:
                s_list.append(i)
        for i in T:
            if i=='#':
                if len(t_list)!=0:
                    t_list.pop()
            else:
                t_list.append(i)
        if t_list == s_list:
            return True
        else:
            return False

if __name__ == '__main__':
    test = Solution()
    judge=test.backspaceCompare("ab#c","ad#c")
    print(judge)