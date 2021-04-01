import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체
sys.setrecursionlimit(10000)


def dfs(X, Y):
    global MAP, M, N
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    MAP[X][Y] = -1
    for i in range(4):
        XX, YY = X + dx[i], Y + dy[i]
        if XX < 0 or XX == M or YY < 0 or YY == N:
            continue
        if MAP[XX][YY] == 1:
            MAP[XX][YY] = -1
            dfs(XX, YY)


T = int(input())                            # 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
for _ in range(T):                          # 그 다음 줄부터 각각의 테스트 케이스에 대해
    M, N, K = map(int, input().split())     # 첫째 줄에는 배추를 심은 배추밭의 가로길이 M 세로길이 N, 그리고 배추가 심어져 있는 위치의 개수 K가 주어진다.
    MAP = [[0]*N for _ in range(M)]
    count = 0
    for _ in range(K):                      # 그 다음 K 줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
        X, Y = map(int, input().split())
        MAP[X][Y] = 1
    for i in range(M):
        for j in range(N):
            if MAP[i][j] > 0:
                dfs(i, j)
                count += 1
    print(count)                            # 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

