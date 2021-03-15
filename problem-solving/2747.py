n = int(input())

def 피보나치():
    sum = 0
    a = 1
    for i in range(n):
        sum, a = a, sum + a
    return sum

print(피보나치())


