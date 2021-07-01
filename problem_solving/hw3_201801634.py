def make_half(n, serving_times, min_times, max_times):
    mid_times = (max_times + min_times) // 2
    acceptable_n = 0

    number_of_staffs = len(serving_times)

    for i in range(number_of_staffs):
        acceptable_n = acceptable_n + (mid_times // serving_times[i])

    if n < acceptable_n:  # 주어진 시간안에 더 많은 사람을 처리할 수 있다
        return make_half(n, serving_times, min_times, mid_times)

    elif n > acceptable_n:  # 주어진 시간 안에 더 적은 사람밖에 처리할 수 없다
        if max_times - mid_times == 1:
            mid_times = (min_times + 1 + max_times + 1) // 2
            return mid_times
        else:
            return make_half(n, serving_times, mid_times, max_times)

    else:
        return mid_times


def min_times_all_served(n, serving_times):
    min_times = 1
    max_times = 1000000000000000000  # 100경

    return make_half(n, serving_times, min_times, max_times)
