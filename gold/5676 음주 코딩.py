"""
    5678 "음주 코딩"
    문제 링크: https://www.acmicpc.net/problem/5676
    
    세그먼트 트리 재귀형식으로 풀었다.
    +,-,0만 가리면 되기때문에 값을 -1, 0, 1만 넣었다.
        
"""

from sys import stdin
input = stdin.readline

def Init(start, end, idx):
    if start == end:
        if arr[start] > 0:
            tree[idx] = 1
        elif arr[start] == 0:
            tree[idx] = 0
        else:
            tree[idx] = -1
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = Init(start, mid, idx*2) * Init(mid+1, end, idx*2+1)
    return tree[idx]
                    
def IntervalProduct(start, end, idx, left, right):
    if right < start or left > end:
        return 1
    if left <= start and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return IntervalProduct(start, mid, idx*2, left, right ) * IntervalProduct(mid+1, end, idx*2+1, left, right)

def update(start, end, idx, idxToChange, value):
    if idxToChange < start or idxToChange > end:
            return tree[idx]
    if start == end:
        if value > 0:
            tree[idx] = 1
        elif value == 0:
            tree[idx] = 0
        else:
            tree[idx] = -1        
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = update(start, mid, idx * 2, idxToChange, value) * update(mid + 1, end, idx * 2 + 1, idxToChange, value)
    return tree[idx]
while True:
    try:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        result = ''
        tree = [1]*len(arr)*4
        Init(0, len(arr)-1,1)

        for _ in range(k):   
            c, i, j = input().split()
            if c == 'C':
                update(1, len(arr), 1, int(i), int(j))
                
            elif c == 'P':
                product = IntervalProduct(1, len(arr), 1,  int(i), int(j))
                if product > 0:
                    result += '+'
                elif product == 0:
                    result += '0'
                else:
                    result += '-'
        print(result)
    except Exception:
        break