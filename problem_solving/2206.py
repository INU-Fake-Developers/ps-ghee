import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]                                                  # 행 위치 이동
dy = [0, 0, -1, 1]                                                  # 열 위치 이동


def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(M)] for i in range(N)]         # N × M의 행렬, N 줄에 M 개, N 행 M 열
    #print(visit)
    print()
    visit[0][0][1] = 1                                              # 시작하는 첫 번째 칸
    print(visit)
    print()

    while q:
        a, b, w = q.popleft()                                       # 가로위치, 세로위치, 벽뚫여부(겸 이동한 거리)
        if a == N - 1 and b == M - 1:                               # 도착했을 경우 (N x M 이므로 인덱스 최댓값은 N-1, M-1)
            print("visit[a][b][w]: ", visit[a][b][w])
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]                                           # x 이동
            y = b + dy[i]                                           # y 이동
            print("x, y: ", x, y)

            if 0 <= x < N and 0 <= y < M:                           # 맵 범위 내에 있다면
                print("map_input[x][y]: ", map_input[x][y])
                print()
                if map_input[x][y] == 1 and w == 1:                 # 벽이고, 벽뚫 가능
                    visit[x][y][0] = visit[a][b][1] + 1             # 이동한 거리 1 증가
                    q.append([x, y, 0])                             # 벽뚫횟수 1회 소모 완료
                elif map_input[x][y] == 0 and visit[x][y][w] == 0:  # 갈 수 있는 곳이고, 벽뚫 불가능
                    visit[x][y][w] = visit[a][b][w] + 1             # 이동한 거리 1 증가
                    q.append([x, y, w])                             # 현재 정보 저장
                else:                                               # 벽이지만, 벽뚫 불가능
                    pass
                print("visit[a][b][w]: ", visit[a][b][w])
                print("x, y, w: ", x, y, w)
                print()
    return -1


N, M = map(int, input().split())                                    # 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
map_input = []
for i in range(N):
    map_input.append(list(map(int, list(input().strip()))))                 # 입력한 값을 토대로 맵 형성
print(bfs())
