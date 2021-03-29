# TODO : 이중 for 문 최적화

import sys
input = sys.stdin.readline                          # 시간 최적화 - input 을 readline 으로 대체


def shortest_job_first():
    sum_of_time_minimum = 0
    time.sort()                                     # 시간 오름차순 정렬(빨리 끝나는 것부터 처리) 31432 -> 12345
    for i in range(N):                              # N번 더해야 하니까
        for j in range(i + 1):                      # 이전에 걸린 시간까지 누적해서 더해야 하니까
            sum_of_time_minimum += time[j]          # 1 + (1+2) + (1+2+3) + (1+2+3+3) = 32
    return sum_of_time_minimum                      # 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값


N = int(input())                                    # 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다
time = list(map(int, input().split()))              # 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다

print(shortest_job_first())
