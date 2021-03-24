import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체


def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0
    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0


n, m, v = map(int, input().split())             # 첫째 줄에 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V가 주어진다.
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1

dfs(v)
print()
bfs(v)
