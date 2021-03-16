import sys
input = sys.stdin.readline                  # 시간 최적화 - input 을 readline 으로 대체

N = int(input())                            # 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
array = []
for i in range(N):                          # 둘째 줄부터 N개의 줄에는 숫자가 주어진다
    array.append(int(sys.stdin.readline()))
for i in sorted(array):                     # 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를
    print(str(i))                           # 한 줄에 하나씩 출력한다.
