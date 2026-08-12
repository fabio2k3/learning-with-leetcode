class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lis = []

        for interval in intervals:
            lis.append((interval[0], "O"))
            lis.append((interval[1], "C"))

        lis.append((newInterval[0], "O"))
        lis.append((newInterval[1], "C"))

        lis.sort(key=lambda x: (x[0], 0 if x[1] == "O" else 1))
        
        p = 0
        
        count_Open = 1
        count_Close = 0
        
        res = []
        
        for i in range(1, len(lis)):
            if lis[i][1] == "C":
                count_Close += 1
        
            if lis[i][1] == "O":
                if count_Open == 0:
                    p = i
                count_Open += 1
                    
            if count_Open == count_Close:
                interval = []
                interval.append(lis[p][0])
                interval.append(lis[i][0])
                res.append(interval)
                count_Open = 0
                count_Close = 0
        
        return res