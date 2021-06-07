"""
    1. 두 문자열 숫자 입력
    2. 유효성 검사 - 숫자와 음수 부호(-)만 가능
        1) 0번 인덱스에 음수 부호가 붙어있는가?
        2) 그 이후 모두 숫자인가?
        3) 최소 두 개?
    3. 덧셈
    4. -- ++ +- -+
    ++은 클리어, +-와 -+은 하나로, --는 ++ 후 부호 붙이기
    1 + 1   -1 + -1    1 + -1   -1 + 1
    1 - 1   -1 - -1    1 - -1   -1 - 1

    5. 덧셈과 뺄셈은 종이 한 장 차이다. 뺄셈도 덧셈처럼 깔끔하게 처리할 수 있지 않을까?

    234
  - 456
  -------
"""
import re


def add(a, b):
    _unexpected_input_exception(a, b)

    a, b = _fit_length(a, b)

    a_negative = _is_negative(a)
    b_negative = _is_negative(b)

    if not a_negative and not b_negative:
        return _add_non_negatives_fixed_length(a, b)
    elif a_negative and b_negative:
        return '-' + _add_non_negatives_fixed_length(a.lstrip('-'), b.lstrip('-'))
    elif a_negative or b_negative:
        if a_negative:
            return _subtract_non_negatives_fixed_length(b, a)
        else:
            return _subtract_non_negatives_fixed_length(a, b)


def _is_negative(number):
    return number[0] == "-"


def _fit_length(a, b):
    sign_a, number_a = _extract_sign_and_number(a)
    sign_b, number_b = _extract_sign_and_number(b)

    if len(number_a) > len(number_b):
        how_many = len(number_a) - len(number_b)
        number_b = ('0'*how_many) + number_b
    elif len(number_a) < len(number_b):
        how_many = len(number_b) - len(number_a)
        number_a = ('0' * how_many) + number_a
    else:
        pass

    return sign_a + number_a, sign_b + number_b


def _extract_sign_and_number(number):

    if _is_negative(number):
        return number[0], number[1:]
    else:
        return '', number


def _change_sign(a):
    if _is_negative(a):
        return a[1:]
    else:
        return "-" + a


def subtract(a, b):
    _unexpected_input_exception(a, b)

    return add(a, _change_sign(b))


def _add_non_negatives_fixed_length(a, b):
    """
    Add a and b.

    :param a: MUST BE > 0
    :param b: MUST BE > 0
    :return: string representation of a + b.
    """
    carry = 0
    answer = []
    for i in range(-1, -(len(a)+1), -1):
        digit_a = int(a[i])
        digit_b = int(b[i])

        sum_hbd = (digit_a + digit_b + carry) % 10
        carry = (digit_a + digit_b + carry) // 10

        answer.append(sum_hbd)

    if carry != 0:
        answer.append(carry)

    answer.reverse()
    while answer[0] == 0 and len(answer) >= 2:
        del answer[0]

    return ''.join(map(str, answer))


def _is_right_bigger(a, b):
    if a == b:
        return False

    sorted_a, sorted_b = sorted([a, b])

    return (sorted_a, sorted_b) == (a, b)


def _subtract_non_negatives_fixed_length(a, b):
    """
    Subtract b from a.

    :param a: MUST BE >= 0
    :param b: MUST BE > 0
    :return: string representation of a - b.
    """
    answer_will_be_negative = False

    if _is_right_bigger(a, b):
        # Ensure left bigger
        a, b = b, a
        answer_will_be_negative = True

    return ('-' if answer_will_be_negative else '') + _subtract_small_from_big(a, b)


def _subtract_small_from_big(big, small):
    borrow = 0
    answer = []

    for i in range(-1, -(len(big) + 1), -1):
        digit_a = int(big[i])
        digit_b = int(small[i])

        borrowed = False
        if digit_a < (digit_b + borrow):
            # Have to borrow
            if i != -len(big):
                borrowed = True
                digit_a += 10

        sub_hbd = digit_a - (digit_b + borrow)

        borrow = 0 if not borrowed else 1

        answer.append(sub_hbd)

    answer.reverse()

    while answer[0] == 0 and len(answer) >= 2:
        del answer[0]

    return ''.join(map(str, answer))


def _unexpected_input_exception(a, b):
    if not re.match('-?[0-9]+', a) or not re.match('-?[0-9]+', b):
        print("잘못된 입력입니다. 프로그램 재시동 후 다시 입력해주세요.")
        exit(1)
    else:
        pass


if __name__ == '__main__':
    print(add('0009', '10'))
    '''
    # test add function
    assert add('1', '2') == '3'
    assert add('9', '5') == '14'
    assert add('19', '2') == '21'
    assert add('15', '2') == '17'
    assert add('1234567890', '1234567890') == '2469135780'
    assert add('-1', '-2') == '-3'
    assert add('2', '-1') == '1'
    assert add('0', '0') == '0'
    assert add('-0', '-0') == '-0'

    # test subtract function
    assert subtract('-2', '-1') == '-1'
    assert subtract('2', '-1') == '3'
    assert subtract('-2', '1') == '-3'
    assert subtract('1', '2') == '-1'
    assert subtract('2', '1') == '1'
    assert subtract('100', '92') == '8'
    assert subtract('0', '0') == '0'

    print("all test passed")
    '''



