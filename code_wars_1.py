"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23. Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number
passed in. Additionally, if the number is negative, return 0. Note: If the number is a multiple of both 3 and 5,
only count it once.

"""


def my_func(num_check: int) -> int:
    hold_num: list[int] = []
    start_val: int = num_check - 1

    if num_check < 0:
        hold_num.append(0)
    else:
        while start_val > 0:
            if start_val % 3 == 0 or start_val % 5 == 0:
                hold_num.append(start_val)
            start_val -= 1

    print(hold_num)
    return sum(hold_num)


if __name__ == '__main__':
    print(my_func(16))
