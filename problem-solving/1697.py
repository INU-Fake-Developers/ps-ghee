from collections import deque
import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체


def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v] + 1
                q.append(next_step)


MAX = 100001
N, K = map(int, input().split())
time = [0]*MAX

bfs()