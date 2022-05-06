"""
    1016 "제곱ㄴㄴ수"
    문제 링크: https://www.acmicpc.net/problem/1016
    
    
    에라토스테네스의 체 응용 문제이다.
    min에서 max까지의 수들 중 제곱수의 곱으로 나누어 떨어지는 수들을 모두 걸러내면 제곱ㄴㄴ수만 남게 된다.
    sNum = (min // square) * square을 하면 sNum은 min 혹은 min보다 한단계 적은 제곱수의 곱이 되는데, 적은 수가 된 경우 제곱수를 한번 더해준다.
            
"""

min, max = list(map(int, input().split()))
ans = max - min + 1
arr = [0 for _ in range(ans)]

i = 2

while (i * i <= max):
    square = i*i
    sNum = (min // square) * square
    if sNum < min:
        sNum += square

    while sNum <= max:
        if arr[sNum - min] == 0:

            arr[sNum - min] = 1
            ans -= 1
        sNum += square
    i += 1
print(ans)