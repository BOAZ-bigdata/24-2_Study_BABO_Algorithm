#14284
import heapq
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
#최단 거리 저장
min_dis = [float('inf')] * (n + 1)

def calc(st):
    min_dis[st] = 0
    q = []
    heapq.heappush(q,(0,st))
    while q:
        dis,pos = heapq.heappop(q)
        if min_dis[pos] < dis:
            continue
        for l,k in graph[pos]:
            #l : 현재 노드랑 연결된 노드, k: 가중치
            res = dis+k
            if res < min_dis[l]:
                min_dis[l] = res
                heapq.heappush(q,(res,l))


for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t = map(int,input().split())
calc(s)
print(min_dis[t])



#14938
n,m,r = map(int,input().split())
items = list(map(int,input().split()))
res = 0 #최종결과
graph = [[1e9]*(n+1) for _ in range(n+1)]

for _ in range(r):
    a,b,l = map(int,input().split())
    graph[a][b] = l
    graph[b][a] = l

# i =j 일때 다 0처리
for i in range(1, n+1):
    graph[i][i] = 0
    
#i,j 와 i,j,k비교, 3중 반복
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for  re in graph:
    temp = 0
    for i in range(1,n+1):
        if re[i] <= m:
            temp+=items[i-1]
    res = max(temp,res)

print(res)
