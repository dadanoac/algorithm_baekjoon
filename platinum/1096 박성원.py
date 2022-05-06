"""
    1386 "박성원"
    문제 링크:https://www.acmicpc.net/problem/1086
    
    bitmasking과 dp를 이용해 풀었다.
    최대 50자, 원소 15개로 만들어지는 모든 순열을 순회할 경우 시간 제한에 걸린다.
    memorization을 사용하여 이미 탐색한 경우에 대해서는 다시 연산하지 않도록 해야한다. 
    
    리스트 dp는 dp[나머지][이미 방문한 원소의 비트문자열]="방문 가능한 경우의 수들 중 나마지가 0인 순열의 개수" 이다.
    
    아래 나머지의 성질을 이용하면 식이 단순화되고, 리스트 dp의 1차 사이즈는 k가 된다. 
    예를 들어 arr=[5221,40] 이라고 했을 때,
        mod(522140, k) = mod(mod(522100, k) + mod(40, k))
                       = mod(mod(mod(5221, k)*mod(100,k),k)+mod(40, k))
"""

from math import factorial, gcd
import sys
input = sys.stdin.readline

def bfs(rest, used):
    if used == ((1 << n)-1):
        if rest == 0:
            return 1
        else:
            return 0

    if dp[rest][used] != -1:
        return dp[rest][used]
    temp = 0
    for i in range(n):
        if not used & (1 << i):
            newRest = ((rest*mod_k[numsLen[i]])%k + nums[i]) % k
            temp += bfs(newRest, used | (1 << i))
    dp[rest][used] = temp
    return dp[rest][used]

n = int(input())
nums = [int(input()) for _ in range(n)]
k = int(input())
dp = [[-1]*(1 << n) for _ in range(k)]
numsLen = [len(str(i)) for i in nums]
nums = [i % k for i in nums]

mod_k = [1]
for i in range(50):
    mod_k.append((mod_k[-1]*10) % k)
p = bfs(0, 0)

q = factorial(n)
temp = gcd(q,p)

print('{}/{}'.format(p//temp, q//temp))