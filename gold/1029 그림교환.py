"""
    1029 "그림교환"
    문제 링크: https://www.acmicpc.net/problem/1029

    bitmasking과 dp를 이용해 풀었다.
"""
n = int(input())
valueMap = [list(int(i) for i in input()) for _ in range(n)]

dp = [[1]*(1 << n) for _ in range(n)]


def dfs(curValue, x, visited):

    if dp[x][visited] != 1:                                     #이미 최대값을 구한 경우 리턴.
        return dp[x][visited]
            
    for i in range(1, n):
        if (visited & (1 << i)) or (valueMap[x][i] < curValue):     # 이미 방문 했거나 현재 구매한 가격보다 적을 경우 pass
            continue
        dp[x][visited] = max(dp[x][visited], dfs(valueMap[x][i], i, visited | (1 << i)) + 1) 
    return dp[x][visited]
    

print(dfs(0, 0, 1))