import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(y, x, count):
    q = [[y, x]]
    while q:
        now = q.pop(0)
        for i in range(8):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if 0 <= nx < w and 0 <= ny < h and mat[ny][nx] == 1:
                mat[ny][nx] = count
                q.append([ny, nx])


while True:
    w, h = map(int, input().split())                                # 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다
    if w == 0 and h == 0:
        break
    mat = []
    for i in range(h):                                              # 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
        mat.append(list(map(int, input().split())))
    count = 2
    for i in range(h):
        for j in range(w):
            if mat[i][j] == 1:
                count += 1
                bfs(i, j, count)
    print(count - 2)                                                # 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
