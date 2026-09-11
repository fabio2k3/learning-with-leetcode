class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        res_Lis = [1]*n

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                 res_Lis[i] = res_Lis[i-1] + 1

        for j in range(n-2,-1,-1):
            if ratings[j+1] < ratings[j]:
                res_Lis[j] = max(res_Lis[j+1] + 1, res_Lis[j])

        return sum(res_Lis)

    