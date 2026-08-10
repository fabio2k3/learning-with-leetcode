class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lis_Pos = []

        for interval in intervals:
            lis_Pos.append((interval[0], "O"))
            lis_Pos.append((interval[1], "C"))

        lis_Pos.sort(key=lambda x: (x[0], 0 if x[1] == "O" else 1))

        p = 0

        count_Open = 1
        count_Close = 0

        res = []

        for i in range(1, len(lis_Pos)):
            if lis_Pos[i][1] == "C":
                count_Close += 1

            if lis_Pos[i][1] == "O":
                if count_Open == 0:
                    p = i
                count_Open += 1
            
            if count_Open == count_Close:
                interval = []
                interval.append(lis_Pos[p][0])
                interval.append(lis_Pos[i][0])
                res.append(interval)
                count_Open = 0
                count_Close = 0

        return res

                
