import sys
n, m, r = map(int, input().split())
INF = 999999 
graph = [[INF] * (n + 1) for _ in range(n + 1)]
items = [0] + [int(x) for x in sys.stdin.readline().split()] # 아이템 인덱스 1번 노드 1로 맞추기

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    graph[a][b] = l #양방향 통행 가능
    graph[b][a] = l #양방향 통행 가능

for i in range(n + 1):
    graph[i][i] = 0 #자기 위치는 0으로

# 거쳐가는 경로 전부 계산해서 최소 경로 갱신
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) #바로가는 것이 좋은지, 경유해서 가는게 좋은지


total = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1): # 한 시작점에서 각 도착점들까지
        if graph[i][j] <= m : # 활동반경보다 작거나 같으면
            tmp += items[j] # 도착점 아이템 개수 합산

        total = max(total, tmp) #최대 아이템 개수 갱신

print(total)