# 연결 그래프? -> 모든 정점에 대해서 항상 경로를 가지는 그래프
# 무방향 그래프
import heapq
import sys

input = sys.stdin.readline
n , m = map(int, input().split()) #정점, 간선 수
INF = 999999
distance = [INF] * (n+1) #간선 가중치 초기화
graph = [[] for _ in range(n+1)] #크기만큼 빈 그래프 연결

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) #무방향 그래프로 양방향 연결
    graph[b].append((a, c)) #무방향 그래프로 양방향 연결

def dijkstra(start, target):
    q = []
    heapq.heappush(q, (0, start)) #0, 시작점 쌍 우선순위 큐 넣기
    distance[start] = 0 #거리 초기화 - 시작점
    while q:
        dist, now = heapq.heappop(q) #현재 탐색노드와, 탐색노드까지 거리
        if distance[now] < dist:#비용이 최단거리보다 크면 갱신 x
            continue
        for v, w in graph[now]: #인접 노드 탐색
            cost = dist + w #비용
            if cost < distance[v]: #비용이 최단거리보다 작으면
                distance[v] = cost #최소거리 갱신
                heapq.heappush(q, (cost, v)) #다음탐색 위해 새로운 인접노드 추가
    print(distance[target])# target까지 연결 최소경로

s, t = map(int, input().split())
dijkstra(s, t)