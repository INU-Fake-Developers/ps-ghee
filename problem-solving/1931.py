import sys
input = sys.stdin.readline                          # 시간 최적화 - input 을 readline 으로 대체


def how_many(input_arr):
    max_meeting = 0                                 # 사용할 수 있는 회의의 최대 개수
    end = 0                                         # 이전 회의가 끝난 시각

    for i in range(len(input_arr)):
        if end <= input_arr[i][0]:                  # 정렬된 i 번째 회의 시작 시각이 end 보다 나중이면(= 회의 가능)
            end = input_arr[i][1]                   # i 번째 회의 종료 시각을 갱신
            max_meeting += 1                        # i 번째 회의가 가능하므로 추가
    return max_meeting                              # 정답! 최대 answer 개!!


N = int(input())                                    # 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다
meeting_table = []                                  # 회의실 사용표

for i in range(N):                                  # 주어진 회의 수만큼
    A, B = map(int, input().split())                # 공백을 사이에 두고 회의의 시작시간(A)과 끝나는 시간(B)이 주어진다.
    meeting_table.append([A, B])                    # 구분한 A, B를 묶어 회의실 사용표에 추가한다

meeting_table.sort(key=lambda x: (x[1], x[0]))      # x[1] 오름차순(종료 시각 오름차순)을 토대로 x[0] 오름차순(시작 시각 오름차순)
print(how_many(meeting_table))
