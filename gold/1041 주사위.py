"""
    1041 "주사위"
    문제 링크: https://www.acmicpc.net/problem/1041
    
    그리디알고리즘 사용
    주사위를 N*N*N로 보이는 면이 최소가 되도록 쌓으면 
        한면짜리가 (N-2)(n-1)*4+(N-2)(N-2)개
        두면짜리가 (N-2)*8개
        세면짜리가 4개 보이게 된다.    
    각각 한면만 보이는 주사위, 두면만 보이는 주사위, 세면 보이는 주사위의 최소값을 구해서 위의 개수를 더해주면 된다.
"""

n = int(input())

square = list(map(int, input().split()))

def findTwo(a,b,c,d,e,f):
    return min([a + c, a + b, a + e, a + d, b + c, b + d, b + f, c + e, c + f, e + d, e + f, d + f])
    
def findThree(a,b,c,d,e,f):
    return min([a + b + c, a + c + e, a + d + e, a + b + d, f + b + c, f + c + e, f + d + e, f + b + d])
if n == 1:
    print(sum(square) - max(square))
    quit()
one = min(square)
two = findTwo(*square)
three = findThree(*square)

print((n-1)*4*two + (n-2)*4*two + 4 * three + (n-2)*(n-2)*one + (n-1)*(n-2)*4*one)