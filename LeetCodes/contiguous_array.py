nums: list[int] = [1, 12, -5, -6, 50, 3]
k = 4
new = [nums[i] for i in range(k)]

# for i in range(k):
#     new.append(nums[i])

print(new)
print(sum(new))
avg = round((sum(new) // k), 5)
print(avg)
print()

cumm = []
for i in range(len(nums)):
    if i + k <= len(nums):
        tmp = [num for num in nums[i:i + k]]
        cumm.append(sum(tmp) / k)
        print(tmp)
print()
print(cumm)

print("{:.5f}".format(max(cumm)))


def contiguous(values, j):
    if j != 0 and j <= len(values):
        output = []

        for i in range(len(values)):
            if i + j <= len(values):
                hold = [val for val in values[i:i + j]]
                output.append(sum(hold) / j)

        print("{:.5f}".format(max(output)))


contiguous(nums, k)


# print(type(contiguous(nums, k)))


def contiguous_pro(values, j):
    if j != 0 and j <= len(values):
        output = []

        for i in range(len(values) - j + 1):
            hold = [val for val in values[i:i + j]]
            output.append(sum(hold) / j)

        return max(output)


contiguous_pro(nums, k)
print(type(contiguous_pro(nums, k)))
