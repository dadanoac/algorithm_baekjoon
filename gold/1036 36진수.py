"""
1036번 "36진수"
문제 링크: https://www.acmicpc.net/problem/1036

10진수 -> 36진수: 리스트에 ['01234--XYZ']를 넣어둔 후 수를 36으로 나눠 해당 index의 문자열을 삽입해주면 된다.(decToBase32(dec))
36진수 계산: int(x, 36)사용
그리디알고리즘을 사용했다.
각 하나의 문자가 변경됐을때에 대한 수의 변화는 독립적이므로, 본판일때의 합, 0~Z까지를 하나씩 Z로 변경했을 때의 변화량을 구한 후 역순으로 sort하여
k의 수만큼 본판일때의 합에 변화의 최대치부터 k개만큼을 더해주면 답이 나온다.
답이 0일 때에는 0을 출력한다.
"""
def decToBase32(dec):    
    base32 = ""
    while dec !=0:
        base32 = charList[dec%36] + base32
        dec = dec//36
    return base32

def Base32Sum(chr):
    sum = 0
    
    for i in range(N):
        sum += int(arr[i].replace(chr,'Z'),36)
    return sum

N = int(input())
arr = [input() for _ in range(N)]
k = int(input())
base32Sum = [0] * 36
charList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
original = Base32Sum('-')
for j in range(36): 
    base32Sum[j] += Base32Sum(charList[j]) - original 
base32Sum.sort(reverse=True)

ans = decToBase32(original + sum(base32Sum[0:k]))
if ans:
    print(ans)
else:
    print(0)
