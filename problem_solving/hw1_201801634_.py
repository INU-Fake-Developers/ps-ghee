from typing import List
import sys
import re


def add(left: str, right: str) -> str:
    """
    >>> add('123', '87')
    '210'
    >>> add('0', '1')
    '1'
    >>> add('0', '-20')
    '-20'
    >>> add('37', '-9700')
    '-9663'
    >>> add('99', '10')
    '109'
    """
    assert_number(left)
    assert_number(right)

    digits_left, digits_right = parse(left, right)

    # Carry ignored.
    _, result = add_decimal(digits_left, digits_right)

    return to_string(result)


def subtract(left: str, right: str) -> str:
    """
    >>> subtract('20', '10')
    '10'
    >>> subtract('99', '-10')
    '109'
    >>> subtract('-10', '-10')
    '0'
    """
    assert_number(left)
    assert_number(right)

    return add(left, negate_sign(right))


def assert_number(possibly_a_number: str):
    if not re.match('-?[0-9]+', possibly_a_number):
        raise Exception("Wrong format.")


def parse(left: str, right: str):
    sign_left, digits_left = parse_sign_and_digits(left)
    sign_right, digits_right = parse_sign_and_digits(right)

    # At least two digits must be empty, to prevent overflow and preserve sign.
    pad_to_fit_digits(digits_left, digits_right, extra_padding=2)

    digits_left = digits_left if sign_left > 0 else complement(digits_left)
    digits_right = digits_right if sign_right > 0 else complement(digits_right)

    return digits_left, digits_right


def parse_sign_and_digits(number_as_string: str) -> List[int]:
    """
    >>> parse_sign_and_digits('1234')
    (1, [1, 2, 3, 4])
    >>> parse_sign_and_digits('-15')
    (-1, [1, 5])
    """
    first = number_as_string[0]

    if first == '-':
        number_as_string = number_as_string[1:]

    sign = -1 if first == '-' else 1

    return sign, to_digits(number_as_string)


def to_digits(number_as_string: str) -> List[int]:
    return list(map(int, number_as_string))


def pad_to_fit_digits(digits_left: List[int], digits_right: List[int], extra_padding: int = 1) -> None:
    """
    >>> pad_to_fit_digits([1, 2, 3], [4, 7, 6, 9])
    ([0, 0, 1, 2, 3], [0, 4, 7, 6, 9])
    """
    the_short_one, the_long_one = sorted([digits_left, digits_right], key=lambda l: len(l))

    pad_how_many = len(the_long_one) - len(the_short_one)

    pad_left(the_short_one, 0, pad_how_many + extra_padding)
    pad_left(the_long_one, 0, extra_padding)

    return the_short_one, the_long_one


def pad_left(digits: List[int], with_what: int, how_many: int):
    for _ in range(how_many):
        digits.insert(0, with_what)


def complement(digits: List[int]) -> List[int]:
    """
    >>> complement([0, 1, 2, 3])
    [9, 8, 7, 7]
    >>> complement([9, 9, 0, 1])
    [0, 0, 9, 9]
    """
    nines_complement = list(map(lambda d: 9 - d, digits))
    one = [1]
    pad_left(one, 0, len(digits) - 1)

    _, tens_complement = add_decimal(nines_complement, one)

    return tens_complement


def add_decimal(digits_left: List[int], digits_right: List[int]) -> List[int]:
    """
    >>> add_decimal([3, 6], [4, 2])
    (0, [7, 8])
    >>> add_decimal([9, 3, 7], [0, 9, 9])
    (1, [0, 3, 6])
    >>> add_decimal([9, 9, 9, 5], [0, 0, 0, 3])
    (0, [9, 9, 9, 8])
    """
    if len(digits_left) != len(digits_right):
        raise Exception("Operands should have same length.")

    number_of_digits = len(digits_left)

    result = []
    carry = 0

    for i in range(number_of_digits - 1, -1, -1):
        addition = digits_left[i] + digits_right[i] + carry

        summation = addition % 10
        carry = addition // 10

        result.insert(0, summation)

    return carry, result


def to_string(digits: List[int]) -> str:
    first = digits[0]

    if first == 0:
        joined = ''.join([str(d) for d in digits])
        return joined[:-1].lstrip('0') + joined[-1]
    elif first == 9:
        return '-' + to_string(complement(digits))
    else:
        raise Exception("First digit must be 0 or 9.")


def negate_sign(number_as_string: str) -> str:
    """
    >>> negate_sign('412')
    '-412'
    >>> negate_sign('-1')
    '1'
    """
    first = number_as_string[0]

    if first.isdigit():
        return '-' + number_as_string
    elif first == '-':
        return number_as_string[1:]
    else:
        raise Exception("First character must be '-' or a digit.")


if __name__ == "__main__":
    if sys.flags.interactive:
        print("\n# You can type something like below:\n# >>> add('10', '20')\n# >>> subtract('50', '30')\n")
    else:
        print("Please run with 'python -i main.py'.")
