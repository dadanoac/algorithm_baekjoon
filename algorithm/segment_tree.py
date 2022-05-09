from sys import stdin
input = stdin.readline

arr = list(map(int, input().split()))
n, k = 1, 1
arr = [1,2,3,4,5,6,7,8,9,10]
result = ''
tree = [-1]*len(arr)*4

def Init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = Init(start, mid, idx*2) + Init(mid+1, end, idx*2+1)
    return tree[idx]

def IntervalSum(start, end, idx, left, right):
    if right < start or left > start:
        return 0
    if left <= start and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return IntervalSum(start, mid, idx*2, left, right ) + IntervalSum(mid+1, end, idx*2+1, left, right)

def update(start, end, idx, idxToChange, value):
    if idxToChange < start or idxToChange > end:
            return
    tree[idx] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx * 2, idx, value)
    update(mid + 1, end, idx * 2 + 1, idx, value)

Init(0, len(arr)-1,1)
print(IntervalSum(0, len(arr)-1, 1, 0, 4))
update(0, len(arr) - 1, 1, 0, 4)
print(IntervalSum(0, len(arr) - 1, 1, 0, 2))