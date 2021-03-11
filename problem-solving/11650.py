import sys
input = sys.stdin.readline                          # 시간 최적화 - input 을 readline 으로 대체

N = int(input())                                    # 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다
Coordinates = []                                    # 좌표 리스트

for i in range(N):                                  # 주어진 회의 수만큼
    A, B = map(int, input().split())                # 공백을 사이에 두고 x 좌표와 y 좌표 주어진다.
    Coordinates.append([A, B])                      # 구분한 A, B를 묶어 좌표 리스트에 추가한다

Coordinates.sort(key=lambda x: (x[0], x[1]))        # x[0](x좌) 오름차순을 토대로 x[1]표(y좌표) 오름차순 정렬

for i in range(len(Coordinates)):
    for j in range(len(Coordinates[i])):            # 정렬된 i번째 좌표의 0번 인덱스(x), 1번 인덱스(y) 출력
        print(Coordinates[i][j], end=" ")
    print("")
