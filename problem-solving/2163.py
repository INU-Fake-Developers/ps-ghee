N, M = map(int, input().split())


def cut_chocolate():
    answer = N-1 + (M-1)*N
    return answer


print(cut_chocolate())
