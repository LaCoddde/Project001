import time


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    # print(flowerbed)
    # if n == 0:
    #     return True
    # for i in range(len(flowerbed)):
    #     if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (
    #             i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
    #         flowerbed[i] = 1
    #         n -= 1
    #         if n == 0:
    #             print(flowerbed)
    #             return True
    # return False

    # for i in range(len(flowerbed)):
    #     if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
    #         flowerbed[i] = 1
    #         n -= 1
    #     elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
    #         flowerbed[i] = 1
    #         n -= 1
    #     elif i not in [0, len(flowerbed) - 1] and flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
    #         flowerbed[i] = 1
    #         n -= 1
    #
    # return n == 0

    print(flowerbed)
    if n == 0:
        return True
    
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    print(flowerbed)
                    return True

    return n == 0

    # start_time = time.time()  # Measure start time
    #
    # max_spaces = len(flowerbed) // 2 + len(flowerbed) % 2
    # ones = flowerbed.count(1)
    #
    # end_time = time.time()  # Measure end time
    # runtime = end_time - start_time  # Calculate runtime
    # print("Runtime:", runtime, "seconds")  # Print runtime
    #
    # return ones + n <= max_spaces


print(can_place_flowers([1, 0, 0, 0, 1], 1))
print(can_place_flowers([0, 0, 0, 0, 0], 2))
print(can_place_flowers([0, 0, 1], 1))
print(can_place_flowers([0, 0, 0, 0, 0, 1, 0, 0], 0))
# print(can_place_flowers([0, 1, 0, 0, 1], 3))
