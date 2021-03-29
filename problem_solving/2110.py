import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체

N, C = map(int, input().split())            # 첫째 줄에 집의 개수 N과 공유기의 개수 C가 하나 이상의 빈 칸을 사이에 두고 주어진다.
home = []
for _ in range(N):                          # 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi 가 한 줄에 하나씩 주어진다.
    x = int(input())
    home.append(x)

home.sort()                                 # 우선 수직선상의 집 정렬
nearest = home[1] - home[0]                 # 첫 집과 두 번째 집 거리
farthest = home[-1] - home[0]               # 첫 집과 마지막 집 거리

answer = 0

while nearest <= farthest:
    distance = (nearest + farthest) // 2
    old = home[0]
    count = 1

    for i in range(1, len(home)):
        if home[i] >= old + distance:
            count += 1
            old = home[i]

    if count >= C:
        nearest = distance + 1
        answer = distance
    else:
        farthest = distance - 1

print(answer)
