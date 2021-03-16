import sys
input = sys.stdin.readline                          # 시간 최적화 - input 을 readline 으로 대체

n = int(input())


def 피보나치():
    sum = 0
    a = 1
    for i in range(n):
        sum, a = a, sum + a
    return sum


print(피보나치())


