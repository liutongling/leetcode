#problem description
#Given a string S,check if the letters can be rearranged so that two characters that are adjacent to
#each other are not the same
#if possible, output any possible result, if not possible, return the empty string
class Solution:
    def reorganizeString(self, S: str) -> str:
        #创建一个字典
        dictSting = {}
        for i in S:
            if i in dictSting:
                dictSting[i]+=1
            else:
                dictSting[i] = 1
        #print(dictSting)
        newString = ""
        for key in dictSting:
            newString+=key
            dictSting[key]-=1

        newlist = list(newString)
        while len(newlist)!=len(S):
            i=0
            while i<len(newlist):
                while dictSting:
                    if i ==0 :
                        if key!=newlist[0]:
                            newlist.insert(i,key)
                            dictSting[key]-=1
                            if dictSting[key]==0:
                                dictSting.pop(key)
                            i+=1
                        else:
                            continue
                    if i == len(newlist) - 1:
                        if key!=newlist[-1]:
                            newlist.insert(i, key)
                            dictSting[key] -= 1
                            if dictSting[key]==0:
                                dictSting.pop(key)
                            i+=1
                        else:
                            continue
                    if key!=newlist[i-1] and key!=newlist[i]:
                        newlist.insert(i,key)
                        dictSting[key] -= 1
                        if dictSting[key] == 0:
                            dictSting.pop(key)
                        i+=1
                    else:
                        i+=1
                        continue
        return newString

    # def reorganizeString(self, S: str) -> str:
    #     dictSting = {}
    #     for i in S:
    #         if i in dictSting:
    #             dictSting[i] += 1
    #         else:
    #             dictSting[i] = 1
    #     #选择一个数量重复最大的一个
    #     # number = max(dictSting)
    #     #遍历字典寻找字典数值最大的并且记录他的key键
    #     value = dictSting[S[0]]
    #     k = ""
    #     for key in dictSting:
    #         if value<dictSting[key]:
    #             value = dictSting[key]
    #             k = key
    #     value+=1
    #     if value==len(S)-value

if __name__ == '__main__':
    s = Solution()
    s1 = s.reorganizeString("vvvlo")
    print("")