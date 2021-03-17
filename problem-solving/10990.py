import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체

N = int(input())                            # 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

for i in range(1, N+1):
    if i == 1:
        print(' ' * (N-i) + '*')
    else:
        print(' ' * (N-i) + '*' + ' '*(2*i-3) + '*')
