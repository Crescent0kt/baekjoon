def solution(n):
    def dfs(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            return 1
        result = 0
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                result += dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        return result
    return dfs([], [], []) 