"""
    2150 "Strongly Connected Component"
    문제 링크: https://www.acmicpc.net/problem/2150
    
    SCC문제이다.
"""

import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
v, e = map(int, input().split())
ab = [list([]) for _ in range(v+1)]

for _ in range(e):
    u, w = map(int, input().split())    
    ab[u].append(w)

stack = []                  # 방문하는 노드들을 stack에 쌓는다
visited = [0]*(v+1)         # 한번이라도 방문했으면 1으로 set
finished = [0]*(v+1)        # SCC구성을 끝낸 노드는 finished를 set
nodeId = [0]*(v+1)          # graph의 번호와는 별개로 노드를 방문할 때마다 증가하는 수의 ID를 부여한다. 이 ID를 통해 부모 노드인지 확인할 수 있다.
answer = []                 # 구성된 SCC가 삽입되는 리스트
d = 0
def dfs(idx):
    global d                
    d += 1 
    nodeId[idx] = d                         # node ID 부여
    parent = d                              # 초기 parent값은 자신의 node ID
    stack.append(idx)                       # stack에 삽입한다.
    visited[idx] = 1                        # visited를 1로 set한다.

    for i in ab[idx]:                          # 현재 노드에서 갈 수 있는 노드들 순회
        if visited[i] == 0:                        # 만약 한번도 방문하지 않은 곳이면, 자식노드이다. 하지만 자식노드의 dfs에서 더 낮은 수의 부모노드를 리턴하면 그 값을 parent에 넣는다.
            parent = min(parent, dfs(i))
        elif finished[i] == 0:                      # 이미 방문했는데 finished가 nodeId[i]가 현재 parent보다 작으면 새로운 parent 가 된다.
            parent = min(parent, nodeId[i])
    if nodeId[idx] == parent:                       # nodeId와 parent가 같으면 스택에 쌓인 데이터를 현재 idx의 데이터까지 꺼낸다.
        ssg = []
        while True:
            temp = stack.pop()
            finished[temp] = 1
            ssg.append(temp)            
            if idx == temp:
                break
        answer.append(sorted(list(ssg)))
    return parent

for i in range(1, v+1):
    if visited[i] == 0: 
        dfs(i)
print(len(answer))
for i in sorted(answer):
    print(*i, -1)
