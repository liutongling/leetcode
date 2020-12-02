class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        longArea = len(intervals)
        preArea = 0
        res = []
        #计算两个特殊的
        if longArea == 0:
            return [newInterval]
        elif newInterval[0] > intervals[longArea - 1][1]:
            return intervals.append(newInterval)
        elif newInterval[1] < intervals[0][0]:
            return intervals.insert(0, newInterval)
        elif longArea ==1:
            if intervals[0][0]<newInterval[0] and intervals[0][1] >newInterval[1]:
                return intervals
            elif intervals[0][0]<newInterval[0] and intervals[0][1] < newInterval[1]:
                return  [intervals[0][0],newInterval[1]]
            elif intervals[0][0] >newInterval[0] and intervals[0][1] > newInterval[1]:
                return [newInterval[0],intervals[0][1]]
            else:
                return [newInterval]
        while preArea<longArea:
            if intervals[preArea][1]<newInterval[0]:
                res.append(intervals[preArea])
                preArea+=1
            else:
                recordPre = intervals[preArea][0]

                lastArea = preArea+1

                while lastArea<longArea:
                    if intervals[lastArea][1]<newInterval[1]:
                        lastArea+=1
                    else:
                        if newInterval[1] >= intervals[lastArea][0]:
                        #res.append([recordPre,intervals[lastArea][1]])
                            res.append([recordPre, intervals[lastArea][1]])
                            lastArea+=1
                        else:
                            res.append([recordPre,newInterval[1]])
                        while lastArea < longArea:
                            res.append(intervals[lastArea])
                            return res

if __name__ == '__main__':
    test = Solution()
    lis = test.insert([[1,5],[6,8]],[5,6])
    print(lis)
