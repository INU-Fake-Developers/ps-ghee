import sys
input = sys.stdin.readline      # 시간 최적화 - input 을 readline 으로 대체

N = int(input())                # 첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다.
input_words = []

for i in range(N):              # 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다.
    input_words.append(input())

dict_words = {}

for word in input_words:
    k = len(word)-1
    for s in word:
        if s in dict_words:
            dict_words[s] += pow(10, k)
        else:
            dict_words[s] = pow(10, k)
        k -= 1
print(dict_words)

# 숫자 리스트 초기화하기
nums = []

# 사전의 값들만으로 이루어진 리스트 초기화하기
for value in dict_words.values():
    nums.append(value)

# 숫자 큰순으로 정렬하기
nums.sort(reverse=True)

# 출력할 값과 곱해야하는 수 초기화하기
result, t = 0, 9

# 값 구하기
for i in range(len(nums)):
    result += nums[i]*t
    t -= 1

print(result)
