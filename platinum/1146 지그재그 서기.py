"""
    1146 "지그재그 서기"
    문제 링크: https://www.acmicpc.net/problem/1146
    
    3948 홍준이의 친위대와 같은 방법으로 풀었다.
    답에 100,000,000을 나눈 나머지를 출력한다.
"""

import sys
input = sys.stdin.readline
N = int(input())

def dfs(l, r, sign):
    if l == 0 and r == 0:
        return 1
        
    if dp[l][r][sign] != -1:
        return dp[l][r][sign]
    temp = 0
    if sign == 1:
        for i in range(r):
            temp += dfs(l+i, r-i-1, 0)
    else:
        for i in range(l):
            temp += dfs(l-i-1, r+i, 1)
        
    dp[l][r][sign] = temp
    return dp[l][r][sign]
 
dp = [[[-1]*2 for _ in range(N)] for _ in range(N)]

if N == 1:
    print(1)
else:
    temp = 0
    for j in range(N):
        temp += dfs(j, N-j-1, 1)

    print((temp*2)%1000000)

