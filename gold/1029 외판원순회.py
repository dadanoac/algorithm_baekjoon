"""
    1029 "외판원 순회"
    문제 링크: https://www.acmicpc.net/problem/1029

    bitmasking과 dp를 이용해 풀었다.
"""

n = int(input())
valueMap = [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)
dp = [[INF]*(1 << n) for _ in range(n)]

def dfs(x, visited):
    if visited == ((1 << n) - 1):
        if valueMap[x][0]:              # 마지막 방문지에서 0으로 돌아갈수 있는 경우 valueMap[x][0] 리턴
            return valueMap[x][0]
        else:                           # 마지막 방문지에서 0으로 돌아갈 수 없는 경우 INF
            return INF
    if dp[x][visited] != INF:           # 현재 방문지에서 이미 최소값을 구한 경우 리턴.
        return dp[x][visited]
    for i in range(1,n):
        if visited & (1 << i) or valueMap[x][i] == 0:       # 이미 방문 했거나 갈 수 없을 경우 pass
            continue

        dp[x][visited] = min(dp[x][visited],dfs(i, visited | (1 << i)) + valueMap[x][i])
    return dp[x][visited]

print(dfs(0, 1))