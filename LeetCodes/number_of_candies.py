def kids_with_candies(candies: list[int], extracandies: int) -> list[bool]:
    result: list[bool] = []
    for i in candies:
        hold = i + extracandies
        templist = candies[:]
        templist.remove(i)
        result.append(all(hold >= x for x in templist))

    return result


# def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#     maxCandies = max(candies)
#     result = []
#     for i in range(len(candies)):
#         if candies[i] + extraCandies >= maxCandies:
#             result.append(True)
#         else:
#             result.append(False)
#     return result


print(kids_with_candies([12, 1, 12], 10))
print(kids_with_candies([4, 2, 1, 1, 2], 1))
print(kids_with_candies([2, 3, 5, 1, 3], 3))
