"""
    1. 두 문자열 숫자 입력
    2. 유효성 검사 - 숫자와 음수 부호(-)만 가능
        1) 0번 인덱스에 음수 부호가 붙어있는가?
        2) 그 이후 모두 숫자인가?
        3) 최소 두 개?
    3. 덧셈 -
"""


def add(a, b):
    unexpected_input_exception(a, b)
    carry = 0
    answer = []
    for i in range(-1, -(len(a)+1), -1):
        digit_a = int(a[i])
        digit_b = int(b[i])

        sum_hbd = (digit_a + digit_b + carry) % 10
        carry = (digit_a + digit_b + carry) // 10

        print(digit_a)
        print(digit_b)
        print(carry, sum_hbd)
        answer.append(sum_hbd)
        print(answer)
        print()

    if carry != 0:
        answer.append(carry)

    answer.reverse()

    while len(answer) != 1:
        if answer[0] == 0:
            del answer[0]
    print(a, b)
    print(answer)


def subtract(a, b):
    unexpected_input_exception(a, b)
    print(a, b)


def is_minus_or_digit(char):
    """
    >>> is_minus_or_digit('3')
    True
    >>> is_minus_or_digit('-')
    True
    >>> is_minus_or_digit('a')
    False
    """
    return char == '-' or char in map(str, range(10))


def unexpected_input_exception(a, b):
    if is_minus_or_digit(a[0]):
        pass
    else:
        print("부호 애러: 잘못된 입력입니다. 프로그램 재시동 후 다시 입력해주세요.")
        exit()

    for i in range(len(a)):
        if a[i].isdigit():
            pass
        else:
            print("잘못된 입력입니다. 프로그램 재시동 후 다시 입력해주세요.")
            print(a[i])
            exit()

    if is_minus_or_digit(b[0]):
        pass
    else:
        print("부호 애러: 잘못된 입력입니다. 프로그램 재시동 후 다시 입력해주세요.")
        exit()

    for i in range(len(b)):
        if b[i].isdigit():
            pass
        else:
            print("잘못된 입력입니다. 프로그램 재시동 후 다시 입력해주세요.")
            exit()


if __name__ == '__main__':
    add('0000', '0000')
