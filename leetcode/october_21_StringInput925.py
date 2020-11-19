#925.长按键入
class Solution:
    def isLongPressedName(self,name: str,typed: str)->bool:
        if len(set(name))>len(set(typed)):
            return False
        long_name = len(name)
        long_typed = len(typed)
        typed_index = 0
        name_index = 0
        char = ''
        while name_index <long_name and typed_index<long_typed:
            if name[name_index] == typed[typed_index]:
                char=name[name_index]
                name_index+=1
                typed_index+=1
            elif name[name_index] != typed[typed_index]:
                if typed[typed_index]==char:
                    typed_index+=1
                else:
                    return False
        while typed_index<long_typed:
            if typed[typed_index] != char:
                return False
            typed_index+=1
        if name_index==long_name and typed_index==long_typed:
            return True
        else:
            return False
if __name__ == '__main__':
    test = Solution()
    c=test.isLongPressedName("a","aaaaaaaaa")
    print(c)

