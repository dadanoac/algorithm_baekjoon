"""
    1034 "램프"
    문제 링크: https://www.acmicpc.net/problem/1034

    한 동작에 한열의 모든 램프를 변경할 수 밖에 없으므로 
    똑같이 생긴 행에 대해서만 동시에 모든 램프를 1로 만들 수 있다.
    행의 0의 개수가 홀수이면, k의 값도 홀수, 0의 개수가 짝수이면 k의 값도 짝수이어야 온전히 1로 만들 수 있다.
"""
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
k = int(input())
maxCount = 0

for i in range(n):
    zeroCount = 0
    for j in arr[i]:
        if j == '0':
            zeroCount += 1
    
    if zeroCount%2 == k%2 and zeroCount <= k:
        sameRowCount = 0
        for row in arr:
            if row == arr[i]:
                sameRowCount += 1
        maxCount = max(sameRowCount, maxCount)
print(maxCount)
            