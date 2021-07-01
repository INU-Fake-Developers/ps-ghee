def cnt_cut_squares(m, n):
    if isinstance(m, int) and isinstance(n, int):
        pass
    else:
        return -1

    if 1 <= m and 1 <= n:
        pass
    else:
        return -1

    gcd = find_gcd_of_parameters(m, n)
    return m + n - gcd


def find_gcd_of_parameters(m, n):
    if m < n:
        m, n = n, m
    while m % n != 0:
        c = m % n
        m = n
        n = c
    return n


if __name__ == '__main__':

    assert cnt_cut_squares(12, 8) == 16
    assert cnt_cut_squares(1, 1) == 1
    assert cnt_cut_squares(24, 8) == 24
    assert cnt_cut_squares(0, 1) == -1
    assert cnt_cut_squares(0, 0) == -1
    assert cnt_cut_squares(2, 0) == -1
    assert cnt_cut_squares(-1, 5) == -1
    assert cnt_cut_squares(3, -7) == -1
    assert cnt_cut_squares(3, -7) == -1
    assert cnt_cut_squares(-3, -3) == -1
    assert cnt_cut_squares(2.53, 2) == -1
    assert cnt_cut_squares(3, 0.45) == -1
    assert cnt_cut_squares(3.5, 1.34) == -1
    assert cnt_cut_squares(3.5, -3.2) == -1
    assert cnt_cut_squares(-3.92, 3.14) == -1
    assert cnt_cut_squares(-3.123, -3.87) == -1
    assert cnt_cut_squares('a', 'b') == -1
    assert cnt_cut_squares('a', 3) == -1
    assert cnt_cut_squares('1', '5') == -1

    print('r u sure?')

    print(cnt_cut_squares(12, 8))
    print(cnt_cut_squares(1, 1))
    print(cnt_cut_squares(24, 8))
    print(cnt_cut_squares(0, 1))
    print(cnt_cut_squares(2.53, 2))
    print(cnt_cut_squares(3.5, 1.34))
    print(cnt_cut_squares('a', 'b'))
