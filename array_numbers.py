# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# (123) 456-7890"


# def create_phone_number(nums: list[int]) -> str:
#     return f"({''.join(map(str, nums[:3]))}) {''.join(map(str, nums[3:6]))}-{''.join(map(str, nums[6:]))}"


def create_phone_number(n) -> str:
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


my_num: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
str_list: list[str] = ["a", "b", "c", "d"]

print(my_num[:3])

print("".join(str_list[:3]))

print(map(str, my_num[:3]))

print("".join(map(str, my_num[:3])))
print(create_phone_number(my_num))
