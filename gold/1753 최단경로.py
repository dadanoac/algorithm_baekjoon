"""
    "1753" 최단경로
    문제 링크: https://www.acmicpc.net/problem/1753
    
    다익스트라 알고리즘
    우선순위를 사용하여 최단거리부터 계산한다.
"""

import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
startNode = int(input())
INF = 200000
graph = [[] for _ in range(v+1)]
for _ in range(e):
    n, m, w = map(int, input().split())
    graph[n].append([m,w])

distArr = [INF] * (v+1)             # 답 리스트를 우선 INF로 초기화
q = []                              # 큐

def dijkstra(node):
    heapq.heappush(q,[0, node])         # 힙에 스타트노드와 거리 0을 푸쉬
    distArr[node] = 0                   # 자기자신이므로 거리는 0 
    while q:
        dist, now = heapq.heappop(q)    # 힙의 데이터 하나를 pop 첫데이터가 weight이므로 가장 weight이 작은 데이터가 빠진다
        if distArr[now] < dist:         # 최단거리가 아니면 스킵
            continue
        for m, w in graph[now]:             # pop된 노드에서 갈 수 있는 노드들 순회
            cost = w + dist                     # 현재 거리 + 다음노드까지의 거리
            if cost < distArr[m]:               # 만약 현재 노드를 거쳐 가는게 더 cost가 적다면,  
                distArr[m] = cost                   # 해당 노드까지의 거리를 변경
                heapq.heappush(q, [cost, m])           # 해당 노드의 거리가 바뀌었으므로 heap에 push

dijkstra(startNode)

for i in distArr[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)