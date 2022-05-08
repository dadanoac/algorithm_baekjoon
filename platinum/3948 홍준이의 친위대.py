"""
    3948 "홍준이의 친위대"
    문제 링크: https://www.acmicpc.net/problem/3948
    
    dp 리스트를 dp[l][r][sign]으로 하여 풀었다. 
    l은 현재수보다 낮은 수의 개수, r은 높은 수의 개수, sign 은 다음 들어와야 할 값이 높은 수인지 낮은수인지를 가리킨다.    
"""
import sys
input = sys.stdin.readline
N = int(input())
arr = list(int(input()) for _ in range(N))

def dfs(l, r, sign):
    if l == 0 and r == 0:                           # 마지막 수까지 탐색하였으면 1을 리턴
        return 1
        
    if dp[l][r][sign] != -1:                        # 이미 최적을 구했으면, 그냥 값을 리턴
        return dp[l][r][sign]
    temp = 0
    if sign == 1:                                   # 다음 수가 높은 수이면, r을 차례대로 탐색
        for i in range(r):
            temp += dfs(l+i, r-i-1, 0)
    else:                                           # 다음 수가 낮은 수이면, l을 차례대로 탐색
        for i in range(l):
            temp += dfs(l-i-1, r+i, 1)
        
    dp[l][r][sign] = temp
    return dp[l][r][sign]

dp = [[[-1]*2 for _ in range(20)] for _ in range(20)]

answer = []
for i in range(1, max(arr)):                        # 입력값 중 가장 높은 값까지의 답을 모두 answer에 저장
    temp = 0
    for j in range(i+1):
        temp += dfs(j, i-j, 1)                      # 각 순서 케이스의 경우의 수가 같으므로 낮음->높음 으로 시작하는 케이스만 구해서 답에 2를 곱해준다.
    answer.append(temp)

for i in arr:                                       # answer에서 답을 차례대로 꺼내어 출력
    if i != 1:
        print(answer[i-2]*2)
    else:
        print(1)