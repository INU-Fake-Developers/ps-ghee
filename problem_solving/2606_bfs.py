import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체

N = int(input())
L = int(input())

graph = [[] for _ in range(N+1)]
graph[0] = [0,0]
visited = [False for _ in range(N+1)]
count = 0

for _ in range(L):
    start, end = map(int, input().split())

    graph[start].append(end)
    graph[end].append(start)


def DFS(graph, start, visited):
    global count
    visited[start] = True
    count += 1

    for i in graph[start]:
        if not visited[i]:
            DFS(graph,i,visited)


DFS(graph,1,visited)

print(count-1)