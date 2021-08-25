import sys

# input = sys.stdin.readline    # 시간 최적화 - input 을 readline 으로 대체

N = str(input())                # readline 은 개행문자까지 받으므로 이 문제에서는 input을 사용한다.
word_list = []                  # 인덱싱 처리된 친구들이 담길 리스트
length_N = len(N)               # len(N)을 변수로 -> 최적화
# print(length_N)
word_list = []                  # 인덱싱 처리된 친구들이 담길 리스트
word_list = []                  # 인덱싱 처리된 친구들이 담길 리스트

# print(word_list)

for i in sorted(word_list):     # 바로 정렬하고 출력
    print(i)

